//#include <SPI.h>
#include <Sabertooth.h>

//global variables

//saber specs
const int front_right_addr = 128;  //front wheels (diff) | right wheels (indep)
const int front_right = 0;
const int back_left_addr = 129;  //back wheels (diff) | left wheels (indep)
const int back_left = 1;
const int dig_belt_addr = 130; //dig and belt
const int dig_belt = 2;
const int dig_motor = 1;
const int belt_motor = 2;
const int num_sabers = 3;

Sabertooth S32[3] = { Sabertooth(128, Serial2), Sabertooth(129, Serial2), Sabertooth(130, Serial2) };  //use Serial2
boolean diff_mode = true;
const int saber_max_forward = 127;
const int saber_max_reverse = -127;
const int saber_off = 0;
int power = 0;    //current power setting of the driving motors

//BBB serial constants
const char drive_addr = '1';
const char dig_addr = '2';
const char belt_addr = '3';
const char override_addr = '4';

const char chan1_opt = '1';
const char chan2_opt = '2';
const char drive_opt = '3';
const char turn_opt = '4';
const char power_opt = '5';
const char ramp_opt = '6';
const char freewheel_opt = '7';
const char stop_opt = '8';
boolean override = false;

//PID parameters
double goal_heading = 0.0;    //target heading for PID
double error = 0.0;    //PID error term
double last_error = 0.0;
double cum_error = 0.0;
double P = 1.0;
double I = 0.0;
double D = 0.0;

//pin definitions
const int CS_pin[] = {22, 23, 24, 25};
const int interrupt_pin[] = {2, 3, 21, 20}; //int.0-3
const int edo_pin[] = {26, 27, 28, 29};
const int pub_heading_pin = A0;

//robot specs
const double robotX = 0.75;   //meters
const double robotY = 1.5;
double wheel_circ = 0.0;  //wheel circumference. use for converting absolute measurements to distance
double zero_turn_rad;

//buffers for the encoders
int pos[] = {0, 0, 0, 0};   //current absolute angular position reading (12 bit res.) 0-4095
int last_pos[] = {0, 0, 0, 0}; //last absolute angluar position reading    (12 bit res.)
double distance_motor[] = {0.0, 0.0, 0.0, 0.0};  //distance traveled by each motor at each measurement
int now_millis[] = {0, 0, 0, 0};
int last_millis[] = {0, 0, 0, 0};
volatile int count[] = {0, 0, 0, 0}; //number of data bits (0-11)
volatile int buff[4][12];
int buff_copy[4][12];

//indexes into encoder buffers
const int fl_enc = 0; 
const int fr_enc = 1;
const int br_enc = 2;
const int bl_enc = 3;

const int sampleT_u = 95969; //usec
const int sampleT_m = 96;

//output variables
double total_distance = 0.0;   //cumulative distance traveled by robot  //CURRENTLY UNUSED
double heading = 0.0;          //manipulated by encoder code
double published_heading;      //normalized heading

void setup() {
  \
  double half_robotX = robotX / 2.0;
  double half_robotY = robotY / 2.0;
  zero_turn_rad = sqrt(half_robotX * half_robotX + half_robotY * half_robotY);

  Serial2.begin(9600);
  Sabertooth::autobaud(Serial2);
  
  Serial.begin(9600);     //for the BBB, to get goal heading and drive speed via USB serial connection

  for (int i = 0; i < 3; i++) {
    S32[i].setRamping(5);
  }
  if (diff_mode) {
    S32[front_right].drive(0);
    S32[back_left].drive(0);
    S32[front_right].turn(0);
    S32[back_left].turn(0);
  }
  
  //  //SPI settings for rotary encoder
  //  SPISettings spi_settings(SPI_CLOCK_DIV8, MSBFIRST, SPI_MODE2); //polarity 1 (idle high), phase 0 (rising edge); 2Mhz CLK
  //  SPI.beginTransaction(spi_settings);
  
  pinMode(pub_heading_pin, OUTPUT);

  for (int i = 0; i < 4; i++) {
    pinMode(CS_pin[i], OUTPUT);
    pinMode(interrupt_pin[i], INPUT);
    pinMode(edo_pin[i], INPUT);

    for (int j = 0; j < 12; j++) {
      buff[i][j] = LOW;
      buff_copy[i][j] = LOW;
    }
  }

  attachInterrupt(0, EDO0, RISING);
  attachInterrupt(1, EDO1, RISING);
  attachInterrupt(2, EDO2, RISING);
  attachInterrupt(3, EDO3, RISING);

}

void loop() {
  int loop_millis = millis();
  read_edo();
  process_edo();
  if ((sampleT_m + loop_millis - millis()) > 1) {
    delay(sampleT_m + loop_millis - millis());
  }
}

////////////ENCODER_METHODS///////////

void read_edo() {
  for (int i = 0; i < 4; i++) {
    count[i] = 0;
    last_millis[i] = now_millis[i];
  }
  for (int i = 0; i < 4; i++) {
    now_millis[i] = millis();
  }
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 12; j++) {
      buff[i][j] = LOW;
    }
  }
  for (int i = 0; i < 4; i++) {
    digitalWrite(CS_pin[i], LOW);
  }
  while (count[0] < 12 && count[1] < 12 && count[2] < 12 && count[3] < 12) {
    //wait for interrupts...
  }
  for (int i = 0; i < 4; i++) {
    digitalWrite(CS_pin[i], HIGH);
  }
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 12; j++) {
      buff_copy[i][j] = buff[i][j];
    }
  }
}

void process_edo() {
  for (int i = 0; i < 4; i++) {
    int d = to_decimal(buff_copy[i], 12);
    last_pos[i] = pos[i];
    pos[i] = d;
    int delta_pos = 0;
    if (pos[i] > last_pos[i]) {
      delta_pos = pos[i] - last_pos[i];
    } else if (pos[i] < last_pos[i]) {
      delta_pos = 4095 - (last_pos[i] - pos[i]);
    }
    distance_motor[i] = (delta_pos / 4095.0) * wheel_circ;
  }
  double dist_left = (distance_motor[fl_enc] + distance_motor[bl_enc]) / 2.0;
  double dist_right = (distance_motor[fr_enc] + distance_motor[br_enc]) / 2.0;
  double dh = abs(dist_left - dist_right) / zero_turn_rad; //radians
  dh = dh * 180 / 3.14159;
  if (dist_left > dist_right) {
    dh *= -1;
  }
  heading += dh;
  if (heading >= 360){
    heading = heading - 360;
  } else if (heading < 0){
    heading = 360 - heading;
  }
  
}

int to_decimal(int* b, int len) {
  int sum = 0;
  for (int i = 0; i < len; i++) {
    sum += b[i] * pow(2, i);
  }
  return sum;
}

void EDO0() {
  buff[0][count[0]] = digitalRead(edo_pin[0]);
  count[0]++;
}
void EDO1() {
  buff[1][count[1]] = digitalRead(edo_pin[1]);
  count[1]++;
}
void EDO2() {
  buff[2][count[2]] = digitalRead(edo_pin[2]);
  count[2]++;
}
void EDO3() {
  buff[3][count[3]] = digitalRead(edo_pin[3]);
  count[3]++;
}

void SerialEvent(){
  //address is 1 byte (drive|dig|belt)
  //header is 1 byte (chan1|chan2|drive|turn|power|ramp|freewheel)
  //data is 2 bytes
  char addr;
  char header;
  byte data[] = {0,0};
  int byte_count = 0;
  while(Serial.available() && byte_count < 4){
    if(byte_count==0){
      addr = (char)(Serial.read());
    } else if(byte_count == 1){
      header = (char)(Serial.read());
    } else {
      data[byte_count-1] = Serial.read();
    }
    byte_count++;
  }
  if(addr == drive_addr) {
    if(header == drive_opt){
      drive(data);
    } else if(header == turn_opt){
      turn(data);
    } else if(header == power_opt){
    } else if(header == ramp_opt){
    } else if(header == freewheel_opt){
    } else if(header == stop_opt){
      S32[front_right].stop();
      S32[back_left].stop();
    }
  } else if(addr == dig_addr) {
    if(header == stop_opt){
      S32[dig_belt].motor(dig_motor, saber_off);
    } else {
      dig(data);
    }    
  } else if(addr == belt_addr) {
    if(header == stop_opt){
      S32[dig_belt].motor(belt_motor, saber_off);
    } else {
      belt(data);
    }
  } else if(addr == override_addr) {
    if(header == stop_opt){
      stop_all();
    } 
  }
  if(header == override_char){
    override = true;
  }

}

void drive(byte data[]){
  power = intval(data);  
  S32[front_right].drive(power);
  S32[back_left].drive(power);
  if(!override){
    goal_heading = heading;
    pid_drive();
  }
  override = false;
}

void turn(byte data[]){  
  int d = intval(data);
  if(!override){
    S32[front_right].turn(power);
    S32[back_left].turn(power);
    goal_heading = d;   
    pid_drive();
  } else {
    S32[front_right].turn(d);
    S32[back_left].turn(d);
  }
  override = false;
}

void pid_drive(){
  error = goal_heading - heading;
  double turn,p,i,d,norm_turn;
  while(error > 0.1){
    p = P * error;
    d = D * (error - last_error) / (sampleT_m * 0.001);
    i = I * cum_error;
    turn = p+i+d;
    
    int max_res = (saber_max_forward - saber_max_reverse)/2;
    double scaled = (turn/180.0) * max_res;
    norm_turn = saber_off + (int)(scaled);
    
    S32[front_right].turn(norm_turn);
    S32[back_left].turn(norm_turn);
    
    error = goal_heading - update_heading(); //this may cause issues...
  }
}
double update_heading(){
  return heading;
}

void dig(byte data[]){
  int p = intval(data);
  S32[dig_belt].motor(dig_motor, p);
}

void belt(byte data[]){
  int p = intval(data);
  S32[dig_belt].motor(belt_motor, p);
}

void stop_all(){
  for(int i=0; i < num_sabers; i++){
    S32[i].stop();
  }
}

//SerialEvent2() not needed, TX only

int intval(byte b[]){
  //assume MSB is first, 2 bytes
  int hi;
  int lo; 
  byte mask = B00000001;
  for(int i = 0; i < 8; i++){
    lo += (mask & b[0]) * pow(2,i);
    hi += (mask & b[1]) * pow(2,i);
    mask << 1; 
  }
  hi *= 256;
  return hi+lo;
}
