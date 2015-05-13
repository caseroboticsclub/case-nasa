import serial

class SaberSender:

    SET_VALUE = 0
    SET_KEEP_ALIVE = 16
    SET_SHUTDOWN = 32
    SET_TIMEOUT = 64
    GET_VALUE = 0
    GET_BATTERY = 16
    GET_CURRENT = 32
    GET_TEMPERATURE = 64

    def __init__(self, port, baud=9600):
        if port not in serial.tools.list_ports:
            print('error: port %s not found. will attempt connection anyways.'%(port))
        self.talker = serial.Serial(port, baud)
        self.address = 128

    '''@param int addr  the address of the sabertooth
       @param int command   the command number
       @param int val   the command value
       @param list data     extra bytes of data for the command
       @param int size      the number of extra bytes of data
       @return list     the buffer into which everything has been written'''
    def _write_command(self, addr, command, val, data, size):
        buff = []
        buff.append(addr)
        buff.append(command)
        buff.append(val)
        buff.append(addr + command + val) & 127
        if not size: return buff
        data_chksum = 0
        for i in range(size):
            buff.append(data[i])
            data_chksum += data[i]
        buff.append(data_chksum & 127)
        return buff

    def _write_set_command(self, addr, setType, targetType, targetNumber, val):
        data = []
        if val < 0:
            val *= -1
            setType += 1
        data.append((val >> 0) & 127)
        data.append((val >> 7) & 127)
        data.append(targetType)
        data.append(str(targetNumber))
        return self._write_command(addr, 40, setType, data, 4)

    def _write_get_command(self, addr, getType, targetType, targetNumber):
        data = []
        data.append(targetType)
        data.append(str(targetNumber)
        return self._write_command(addr, 41, getType, data, 2)

    def getMotorTemp(self,chan):
        to_send = self._write_get_command(self.address, GET_TEMPERATURE, 'M', chan)
        for byte in to_send:
            self.talker.write(byte)
        ret = self.talker.read(4)
        return _b2i(ret[:2])

    def close(self):
        self.talker.close()
        return _write_get_command(self,

    def bindAddress(self, addr):
        self.address = addr

    def _b2i(b):
        # low bits are in the first byte
        hi = 256 * int(b[1].encode('hex'),16)
        lo = int(b[0].encode('hex'),16)
        return hi+lo
