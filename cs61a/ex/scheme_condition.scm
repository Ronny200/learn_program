; returns absolute value
(define (abs_value x) (abs x))
(abs_value -1)

; returns reciprocal value
(define (reciprocal x)
    (if (= x 0) #f (- x)))
(reciprocal -3)

; returns ascii char
; (define (asc x) 
;     (if (or (< x 33) (> x 126)) #f 
;         (integer->char x)))
; (asc 55)

; retruns three real numbers product if numbers all positive
(define (three_product x y z)
    (if (and (> x 0) (> y 0) (> z 0)) (* x y z)))

(three_product 1 2 5)

; cond
(define (free age)
    (cond
        ((or (<= age 3) (>= age 65)) 0)
        ((<= age 6) 0.5)
        ((<= age 12) 1.0)
        ((<= age 15) 1.5)
        ((<= age 18) 1.8)
        (else 2.0)
        ))
(free 14)

; return grade
(define (grade score)
    (cond 
        ((>= score 80) 'A)
        ((>= score 60) 'B)
        ((>= score 40) 'C)
        (else 'D)))
(grade 33)

