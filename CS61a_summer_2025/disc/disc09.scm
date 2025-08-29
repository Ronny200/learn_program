;;; Q1: Pair Up
;;; Return a list of pairs containing the elements of s.
    ;;;
    ;;; scm> (pair-up '(3 4 5 6 7 8))
    ;;; ((3 4) (5 6) (7 8))
    ;;; scm> (pair-up '(3 4 5 6 7 8 9))
    ;;; ((3 4) (5 6) (7 8 9))
    (define (pair-up s)
        (if (<= (length s) 3) (list s)
            (cons (list (car s) (car (cdr s)))
                (pair-up (cdr (cdr s))))

        ))

    (expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
    (expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )

;;; Q2: List Insert
(define (insert element lst index)
    (if (= index 0) (cons element lst)
        (cons (car lst)
            (insert element (cdr lst) (- index 1))))
)

    (expect (insert 2 '(1 7 9) 2) (1 7 2 9))

    (expect (insert 'a '(b c) 0) (a b c))

;;; Q3: Interleave
(define (interleave lst1 lst2)
    (cond
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons
            (car lst1)
            (interleave lst2 (cdr lst1))
            ))
    )
)

(expect (interleave '(1 3 5) '(2 4 6)) (1 2 3 4 5 6))

; Q4: Representing Expressions
; Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))
(+ (* 3 4) 5)
; Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))
; Pair('and', Pair(Pair('<', Pair(1, Pair(0, nil))), Pair(Pair('/', Pair(1, Pair(0, nil))), nil)))
(and (< 1 0) (/ 1 0))


; Q7: Slice It!
(define (get-slicer a b)
  (define (slicer lst)
    (define (slicer-helper c i j)
      (cond 
        ((or (null? c) (<= j 0)) nil)
        ((= i 0) (cons (car c) (slicer-helper (cdr c) 0 (- j 1))))
        (else (slicer-helper (cdr c) (- i 1) (- j 1)))))
    (slicer-helper lst a b))
  slicer)

; DOCTESTS (No need to modify)
(define a '(0 1 2 3 4 5 6))
(define one-two-three (get-slicer 1 4))
(define one-end (get-slicer 1 10))
(define zero (get-slicer 0 1))
(define empty (get-slicer 4 4))

(expect (one-two-three a) (1 2 3))
(expect (one-end a) (1 2 3 4 5 6))
(expect (zero a) (0))
(expect (empty a) ())