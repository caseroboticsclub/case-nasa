; Auto-generated. Do not edit!


(cl:in-package ex-msg)


;//! \htmlinclude ex_msg.msg.html

(cl:defclass <ex_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (msg
    :reader msg
    :initarg :msg
    :type cl:string
    :initform "")
   (first
    :reader first
    :initarg :first
    :type cl:integer
    :initform 0)
   (second
    :reader second
    :initarg :second
    :type cl:integer
    :initform 0))
)

(cl:defclass ex_msg (<ex_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ex_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ex_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ex-msg:<ex_msg> is deprecated: use ex-msg:ex_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ex_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-msg:header-val is deprecated.  Use ex-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'msg-val :lambda-list '(m))
(cl:defmethod msg-val ((m <ex_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-msg:msg-val is deprecated.  Use ex-msg:msg instead.")
  (msg m))

(cl:ensure-generic-function 'first-val :lambda-list '(m))
(cl:defmethod first-val ((m <ex_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-msg:first-val is deprecated.  Use ex-msg:first instead.")
  (first m))

(cl:ensure-generic-function 'second-val :lambda-list '(m))
(cl:defmethod second-val ((m <ex_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-msg:second-val is deprecated.  Use ex-msg:second instead.")
  (second m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ex_msg>) ostream)
  "Serializes a message object of type '<ex_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'msg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'msg))
  (cl:let* ((signed (cl:slot-value msg 'first)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'second)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ex_msg>) istream)
  "Deserializes a message object of type '<ex_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'msg) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'msg) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'first) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'second) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ex_msg>)))
  "Returns string type for a message object of type '<ex_msg>"
  "ex/ex_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ex_msg)))
  "Returns string type for a message object of type 'ex_msg"
  "ex/ex_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ex_msg>)))
  "Returns md5sum for a message object of type '<ex_msg>"
  "de40b4cf0841e7ee17696b7506c4c036")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ex_msg)))
  "Returns md5sum for a message object of type 'ex_msg"
  "de40b4cf0841e7ee17696b7506c4c036")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ex_msg>)))
  "Returns full string definition for message of type '<ex_msg>"
  (cl:format cl:nil "Header header~%string msg~%int32 first~%int32 second~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ex_msg)))
  "Returns full string definition for message of type 'ex_msg"
  (cl:format cl:nil "Header header~%string msg~%int32 first~%int32 second~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ex_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'msg))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ex_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'ex_msg
    (cl:cons ':header (header msg))
    (cl:cons ':msg (msg msg))
    (cl:cons ':first (first msg))
    (cl:cons ':second (second msg))
))
