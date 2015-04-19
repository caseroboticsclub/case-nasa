
(cl:in-package :asdf)

(defsystem "actuator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "actuator_data" :depends-on ("_package_actuator_data"))
    (:file "_package_actuator_data" :depends-on ("_package"))
  ))