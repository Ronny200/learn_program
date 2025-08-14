LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
from math import pi, sqrt


class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1


class Button:
    """A button on a keyboard.

    >>> f = lambda c: print(c, end='')  # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """

    caps_lock = CapsLock()

    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        """Call output on letter (maybe uppercased), then return the button that was pressed."""
        self.pressed += 1
        "*** YOUR CODE HERE ***"
        if self.caps_lock.pressed % 2 != 1:
            self.output(self.letter)
        else:
            self.output(self.letter.upper())
        return self


class Keyboard:
    """A keyboard.

    >>> Button.caps_lock.pressed = 0  # Reset the caps_lock key
    >>> bored = Keyboard()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o']
    >>> bored.keys['l'].pressed
    2

    >>> Button.caps_lock.press()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o', 'H', 'E', 'L', 'L', 'O']
    >>> bored.keys['l'].pressed
    4
    """

    def __init__(self):
        self.typed = []
        self.keys = {
            letter: Button(letter, self.add_to_typed) for letter in LOWERCASE_LETTERS
        }

    def add_to_typed(self, char):
        self.typed.append(char)

    def type(self, word):
        """Press the button for each letter in word."""
        assert all([w in LOWERCASE_LETTERS for w in word]), "word must be all lowercase"
        "*** YOUR CODE HERE ***"
        for w in word:
            self.keys[w].press()


class Shape:
    """All geometric shapes will inherit from this Shape class."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))


class Circle(Shape):
    """A circle is characterized by its radii
    >>> c = Circle("My Circle", 5)
    >>> print(c.area())  # 输出: 78.53981633974483 (π*5²)
    78.53981633974483
    >>> print(c.perimeter())  # 输出: 31.41592653589793 (2π*5)
    31.41592653589793
    """

    def __init__(self, name, radius):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        """Returns the perimeter of a circle (2πr)"""
        "*** YOUR CODE HERE ***"
        return 2 * pi * self.radius

    def area(self):
        """Returns the area of a circle (πr^2)"""
        "*** YOUR CODE HERE ***"
        return pi * self.radius**2


class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. The area can also be done, but it's more inconvenient.
    >>> s = Square("My Square", 4)
    >>> print(s.area())
    16
    >>> print(s.perimeter())
    16
    """

    def __init__(self, name, num_sides, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.num_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        """Returns the perimeter of a regular polygon (the number of sides multiplied by side length)"""
        "*** YOUR CODE HERE ***"
        return self.num_sides * self.side_length


class Square(RegPolygon):
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name, 4, side_length)

    def area(self):
        """Returns the area of a square (squared side length)"""
        "*** YOUR CODE HERE ***"
        return self.side_length**2


class Triangle(RegPolygon):
    """An equilateral triangle
    >>> t = Triangle("My Triangle", 3)
    >>> print(t.area())
    3.8971143170299736
    >>> print(t.perimeter())
    9
    """

    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name, 3, side_length)

    def area(self):
        """Returns the area of an equilateral triangle is (squared side length multiplied by the provided constant"""
        constant = sqrt(3) / 4
        "*** YOUR CODE HERE ***"
        return self.side_length**2 * constant


class Eye:
    """An eye.

    >>> Eye().draw()
    '0'
    >>> print(Eye(False).draw(), Eye(True).draw())
    0 -
    """

    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return "-"
        else:
            return "0"


class Bear:
    """A bear.

    >>> Bear().print()
    ? 0o0?
    """

    def __init__(self):
        self.nose_and_mouth = "o"

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print("? " + left.draw() + self.nose_and_mouth + right.draw() + "?")


class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ? -o-?
    """

    "*** YOUR CODE HERE ***"

    def next_eye(self):
        return Eye(True)


class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ? -o0?
    """

    def __init__(self):
        "*** YOUR CODE HERE ***"
        super().__init__()
        self.status = 0

    def next_eye(self):
        "*** YOUR CODE HERE ***"
        self.status += 1
        return Eye(self.status % 2)
