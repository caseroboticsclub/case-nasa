
(cl:in-package :asdf)

(defsystem "ex-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ex_srv" :depends-on ("_package_ex_srv"))
    (:file "_package_ex_srv" :depends-on ("_package"))
  ))