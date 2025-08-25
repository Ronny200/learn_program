(define (sum lst)
  (define (sum-tail lst result)
    (if (null? lst) result
    (sum-tail (cdr lst) (+ result (car lst)))))
  (sum-tail lst 0)
)
(expect (sum '(1 2 3)) 6)
(expect (sum '(10 -3 4)) 11)


(define (reverse lst)
  (define (reverse-tail lst reve-lst)
    (if (null? lst) reve-lst
      (reverse-tail (cdr lst) (cons (car lst) reve-lst)))
  )
  (reverse-tail lst nil)
)
(expect (reverse '(1 2 3)) (3 2 1))
(expect (reverse '(0 9 1 2)) (2 1 9 0))