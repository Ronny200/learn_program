; define a global variable

(define vhello "Hello world")
(print vhello)

; define a lmbda function
(define fhello (lambda () "Hello world too..."))
(fhello)

; define a parameter function
(define hello (lambda (name) 
    (display "Hello" name "!")))
(hello "Luc")

(define sum_three (lambda (a b c) (+ a b c)))
(sum_three 1 2 3)

(define (sum_three_short a b c) (+  a b c))
(sum_three_short 1 2 3)

; return parameter + 1 or -1
(define (add_param x) (+ x 1))
(add_param 4)

(define (sub_param x) (- x 1))
(sub_param 5)

; converts the degrees to radians
(define pi (* 4 (atan 1.0)))
(define (degress_to_radians deg)
    (* deg (/ pi 180)))
(degress_to_radians 90)

; return displacement
(define (displacement v t)
    (* v t))
(displacement 10 5)

; return flight time
(define (flight vy)
    (/ (* 2 (abs vy)) 9.8))
(flight 10)

; horizontal distance
(define (dx vx t)
    (* vx t))

; distance
(define (distance v ang)
    (dx
        (* v (cos (degress_to_radians ang)))
        (flight (* v (sin (degress_to_radians ang))))))

(distance 40 30)