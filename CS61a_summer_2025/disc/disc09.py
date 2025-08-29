class Pair:
    "A Scheme list is a Pair in which rest is a Pair or nil."

    empty = ""

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest


def print_evals(expr):
    """Print the expressions that are evaluated while evaluating expr.

    expr: a Scheme expression containing only (, ), +, *, and numbers.

    >>> nested_expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))
    >>> print_evals(nested_expr)
    (+ (* 3 4) 5)
    +
    (* 3 4)
    *
    3
    4
    5
    >>> print_evals(Pair('*', Pair(6, Pair(7, Pair(nested_expr, Pair(8, nil))))))
    (* 6 7 (+ (* 3 4) 5) 8)
    *
    6
    7
    (+ (* 3 4) 5)
    +
    (* 3 4)
    *
    3
    4
    5
    8
    """
    if not isinstance(expr, Pair):
        "*** YOUR CODE HERE ***"
        print(expr)
    else:
        "*** YOUR CODE HERE ***"
        print(expr)
        print_evals(expr.first)
        current = expr.rest
        while current is not Pair.empty:
            print_evals(current.first)
            current = current.rest


nested_expr = Pair(
    "+", Pair(Pair("*", Pair(3, Pair(4, Pair.empty))), Pair(5, Pair.empty))
)
print_evals(nested_expr)
