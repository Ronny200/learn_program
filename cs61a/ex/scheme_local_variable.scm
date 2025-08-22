; Recursive
(define ls (list 1 2 3 4 5))

(define (list*2 ls)
    (if (null? ls) nil
        (cons (* 2 (car ls))
            (list*2 (cdr ls))))
)
(list*2 ls)

; retrun the number of list
(define (my_length ls)
    (if (null? ls) 0
        (+ 1 (my_length (cdr ls)))
    )
)
(my_length ls)

; summation list number
(define (sum_ls ls)
    (if (null? ls) 0
        (+ (car ls) (sum_ls (cdr ls)))))
(sum_ls ls)

; remove x in list
; (define (remove x lst)
;     (if (null? lst)
;         '()
;         (let ((h (car lst)))
;             ((if (eqv? x h)
;                 (lambda (y) y)
;                 (lambda (y) (cons h y)))
;             (remove x (cdr lst))))))

; (remove 3 ls)

(define (remove x lst)
    (if (null? lst) nil
        (let ((h (car lst))) 
            (if (eqv? x h)
                (remove x (cdr lst))
                (cons (car lst) (remove x (cdr lst))))))
)


(remove 3 ls)

; return x index in list
(define (position x lst i)
    (cond
        ((null? lst) #f)
        ((eqv? x (car lst)) i)
        (else (position x (cdr lst) (+ 1 i)))
    )
)

(position 2 ls 0)

; reverse list
(define (reverse_lst lst new_lst)
    (if (null? lst) new_lst
        (reverse_lst (cdr lst) (cons (car lst) new_lst)))
)
(reverse_lst ls '())


; summation list
(define (sum_list lst total)
    (if (null? lst) total
        (sum_list (cdr lst) (+ total (car lst))))
        
)
(sum_list ls 0)

