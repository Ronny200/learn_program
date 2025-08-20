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
