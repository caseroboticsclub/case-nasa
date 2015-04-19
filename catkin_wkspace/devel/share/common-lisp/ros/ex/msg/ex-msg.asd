
(cl:in-package :asdf)

(defsystem "ex-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ex_msg" :depends-on ("_package_ex_msg"))
    (:file "_package_ex_msg" :depends-on ("_package"))
  ))