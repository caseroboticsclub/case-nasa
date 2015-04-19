; Auto-generated. Do not edit!


(cl:in-package ex-srv)


;//! \htmlinclude ex_srv-request.msg.html

(cl:defclass <ex_srv-request> (roslisp-msg-protocol:ros-message)
  ((first
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

(cl:defclass ex_srv-request (<ex_srv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ex_srv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ex_srv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ex-srv:<ex_srv-request> is deprecated: use ex-srv:ex_srv-request instead.")))

(cl:ensure-generic-function 'first-val :lambda-list '(m))
(cl:defmethod first-val ((m <ex_srv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-srv:first-val is deprecated.  Use ex-srv:first instead.")
  (first m))

(cl:ensure-generic-function 'second-val :lambda-list '(m))
(cl:defmethod second-val ((m <ex_srv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-srv:second-val is deprecated.  Use ex-srv:second instead.")
  (second m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ex_srv-request>) ostream)
  "Serializes a message object of type '<ex_srv-request>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ex_srv-request>) istream)
  "Deserializes a message object of type '<ex_srv-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ex_srv-request>)))
  "Returns string type for a service object of type '<ex_srv-request>"
  "ex/ex_srvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ex_srv-request)))
  "Returns string type for a service object of type 'ex_srv-request"
  "ex/ex_srvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ex_srv-request>)))
  "Returns md5sum for a message object of type '<ex_srv-request>"
  "85a734c776d49ce7e013b15b395d3f69")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ex_srv-request)))
  "Returns md5sum for a message object of type 'ex_srv-request"
  "85a734c776d49ce7e013b15b395d3f69")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ex_srv-request>)))
  "Returns full string definition for message of type '<ex_srv-request>"
  (cl:format cl:nil "~%int32 first~%int32 second~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ex_srv-request)))
  "Returns full string definition for message of type 'ex_srv-request"
  (cl:format cl:nil "~%int32 first~%int32 second~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ex_srv-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ex_srv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ex_srv-request
    (cl:cons ':first (first msg))
    (cl:cons ':second (second msg))
))
;//! \htmlinclude ex_srv-response.msg.html

(cl:defclass <ex_srv-response> (roslisp-msg-protocol:ros-message)
  ((sum
    :reader sum
    :initarg :sum
    :type cl:integer
    :initform 0))
)

(cl:defclass ex_srv-response (<ex_srv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ex_srv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ex_srv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ex-srv:<ex_srv-response> is deprecated: use ex-srv:ex_srv-response instead.")))

(cl:ensure-generic-function 'sum-val :lambda-list '(m))
(cl:defmethod sum-val ((m <ex_srv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ex-srv:sum-val is deprecated.  Use ex-srv:sum instead.")
  (sum m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ex_srv-response>) ostream)
  "Serializes a message object of type '<ex_srv-response>"
  (cl:let* ((signed (cl:slot-value msg 'sum)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ex_srv-response>) istream)
  "Deserializes a message object of type '<ex_srv-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sum) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ex_srv-response>)))
  "Returns string type for a service object of type '<ex_srv-response>"
  "ex/ex_srvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ex_srv-response)))
  "Returns string type for a service object of type 'ex_srv-response"
  "ex/ex_srvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ex_srv-response>)))
  "Returns md5sum for a message object of type '<ex_srv-response>"
  "85a734c776d49ce7e013b15b395d3f69")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ex_srv-response)))
  "Returns md5sum for a message object of type 'ex_srv-response"
  "85a734c776d49ce7e013b15b395d3f69")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ex_srv-response>)))
  "Returns full string definition for message of type '<ex_srv-response>"
  (cl:format cl:nil "~%int32 sum~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ex_srv-response)))
  "Returns full string definition for message of type 'ex_srv-response"
  (cl:format cl:nil "~%int32 sum~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ex_srv-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ex_srv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ex_srv-response
    (cl:cons ':sum (sum msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ex_srv)))
  'ex_srv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ex_srv)))
  'ex_srv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ex_srv)))
  "Returns string type for a service object of type '<ex_srv>"
  "ex/ex_srv")