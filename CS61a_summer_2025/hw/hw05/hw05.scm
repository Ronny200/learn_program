(define (square n) (* n n))

(define (pow base exp)
    (cond ((= exp 0) 1)
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (square (pow base (/ (- exp 1) 2)))))
    )
)

; def repeatedly(n, x):
;     if n == 0:
;         return x
;     x = x * x * x
;     return 1 * repeatedly(n - 1, x)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))
