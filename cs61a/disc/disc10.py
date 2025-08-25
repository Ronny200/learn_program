class Tree:
    def __init__(self, label, branches=[]):
        """A tree has a label and a list of branches.

        >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t.label
        3
        >>> t.branches[0].label
        2
        >>> t.branches[1].is_leaf()
        True
        """
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return f"Tree({repr(self.label)}{branch_str})"

    def __str__(self):
        return "\n".join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append("  " + line)
        return [str(self.label)] + lines


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            link_str = ", " + repr(self.rest)
        else:
            link_str = ""
        return f"Link({repr(self.first)}{link_str})"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    "*** YOUR CODE HERE ***"
    total_sum = sum(s)

    def helper(index, current_sum):
        if index == len(s):
            return 1 if abs(2 * current_sum - total_sum) <= d else 0
        count1 = helper(index + 1, current_sum + s[index])
        count2 = helper(index + 1, current_sum)

        return count1 + count2

    return helper(0, 0) // 2


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return False

    slow = link
    fast = link.rest
    while fast is not Link.empty and fast.rest is not Link.empty:
        if slow is fast:
            return True
        slow = slow.rest
        fast = fast.rest.rest
    return False


def in_order_traversal(t):
    """
    Generator function that generates an "in-order" traversal, in which we
    yield the value of every node in order from left to right, assuming that each node has either 0 or 2 branches.

    For example, take the following tree t:
            1
        2       3
    4     5
         6  7

    We have the in-order-traversal 4, 2, 6, 5, 7, 1, 3

    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        yield t.label
    else:
        left, right = t.branches
        yield from in_order_traversal(left)
        yield t.label
        yield from in_order_traversal(right)


def after(s, a, b):
    """Return whether b comes after a in linked list s.
    >>> t = Link(3, Link(6, Link(5, Link(4))))
    >>> after(t, 6, 4)
    True
    >>> after(t, 4, 6)
    False
    >>> after(t, 6, 6)
    False
    """
    "*** YOUR CODE HERE ***"
    if a == b:
        return False
    found_a = False
    while s is not Link.empty:
        if s.first == a:
            found_a = True
        if s.first == b:
            return found_a
        s = s.rest
