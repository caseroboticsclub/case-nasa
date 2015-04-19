; Auto-generated. Do not edit!


(cl:in-package actuator-msg)


;//! \htmlinclude actuator_data.msg.html

(cl:defclass <actuator_data> (roslisp-msg-protocol:ros-message)
  ((height_offset
    :reader height_offset
    :initarg :height_offset
    :type cl:integer
    :initform 0))
)

(cl:defclass actuator_data (<actuator_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <actuator_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'actuator_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name actuator-msg:<actuator_data> is deprecated: use actuator-msg:actuator_data instead.")))

(cl:ensure-generic-function 'height_offset-val :lambda-list '(m))
(cl:defmethod height_offset-val ((m <actuator_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader actuator-msg:height_offset-val is deprecated.  Use actuator-msg:height_offset instead.")
  (height_offset m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <actuator_data>) ostream)
  "Serializes a message object of type '<actuator_data>"
  (cl:let* ((signed (cl:slot-value msg 'height_offset)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <actuator_data>) istream)
  "Deserializes a message object of type '<actuator_data>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height_offset) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<actuator_data>)))
  "Returns string type for a message object of type '<actuator_data>"
  "actuator/actuator_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'actuator_data)))
  "Returns string type for a message object of type 'actuator_data"
  "actuator/actuator_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<actuator_data>)))
  "Returns md5sum for a message object of type '<actuator_data>"
  "42b409eee8002bc6b9d50cfde1aaf409")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'actuator_data)))
  "Returns md5sum for a message object of type 'actuator_data"
  "42b409eee8002bc6b9d50cfde1aaf409")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<actuator_data>)))
  "Returns full string definition for message of type '<actuator_data>"
  (cl:format cl:nil "int32 height_offset~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'actuator_data)))
  "Returns full string definition for message of type 'actuator_data"
  (cl:format cl:nil "int32 height_offset~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <actuator_data>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <actuator_data>))
  "Converts a ROS message object to a list"
  (cl:list 'actuator_data
    (cl:cons ':height_offset (height_offset msg))
))
