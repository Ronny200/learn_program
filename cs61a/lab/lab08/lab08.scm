; (define (over-or-under num1 num2)
;     (if (< num1 num2) -1 
;         (if (= num1 num2) 0 
;             (if (> num1 num2) 1))))

(define (over-or-under num1 num2)
    (cond
        ((< num1 num2) -1)
        ((> num1 num2) 1)
        (else 0)))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
    (if (= b 0) (abs a)
        (gcd b (modulo a b))))

(define (remove item lst) 
    (if (null? lst) nil
        (filter (lambda (x) (not (= x item))) lst)) 
)

(define (duplicate lst)
    (apply append (map (lambda (x) (list x x)) lst))
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (composed f g)
  (lambda (x) (f (g x)))
)



(define (square x) (* x x))
; (define (repeat f n)
;     (if (=  n 1) f 
;         (lambda (x) 
;              (f ((repeat f (- n 1)) x)))))

(define (repeat f n)
    (if (= n 1) f
        (composed f (repeat f (- n 1)))))