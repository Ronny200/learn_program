; Cons is the basic unit that makes up a list
; Cons must have two unit, car and cdr
; If cons only one unit,then cdr must be '() or nil

(cons "hi" "everybody")
(cons 0 nil)
(cons 1 (cons 10 100))
(cons 1 (cons 10 (cons 100 nil)))
(cons "I" (cons "saw" (cons 3 (cons "girls" nil))))
(cons "Sum of" 
    (cons (cons 1 (cons 2 (cons 3 (cons 4 nil))))
        (cons "is" (cons 10 nil))))

(car '(0)) ; 0
(cdr '(0)) ; '()
(car '((1 2 3) (4 5 6))) ; (1 2 3)
(cdr '(1 2 3 . 4)) ; (2 3 . 4)
(cdr (cons 3 (cons 2 (cons 1 nil)))) ; (2 1)


; Use car or cdr to read the list data
(car (list 1 2 3))