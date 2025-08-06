def race(x, y):
    """乌龟始终以每分钟x英尺的速度行走，而兔子则反复以每分钟 y 英尺的速度跑5分钟，然后休息5分钟。返回乌龟首次追上兔子所经过的分钟数

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, "the hare must be fast but not too fast"
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise != hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


def fizzbuzz(n):
    """打印冰雹序列
    如果 i 同时能被 3 和 5 整除，打印 fizzbuzz。
    如果 i 能被 3 整除但不能被 5 整除，打印 fizz。
    如果 i 能被 5 整除但不能被 3 整除，打印 buzz。
    否则，打印数字 i。
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1


def is_prime(n):
    """判断是否是一个质数
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    # if n == 1:
    #     return False
    # i = 2
    # while i < n // 2:
    #     if n % i == 0:
    #         return False
    #     i += 1
    # return True

    if n == 1:
        return False
    num = n // 2
    while num > 1:
        if n % num == 0:
            return False
        num -= 1
    return True


def unique_digits(n):
    """返回正整数n中唯一数字的个数.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n > 0:
        last = n % 10
        n = n // 10
        if not has_digit(n, last):
            count += 1
    return count


def has_digit(n, k):
    """返回k是否为n中的数字。

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False


def ordered_digits(x):
    """判断x是否为递减的数字
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        return True
    while x > 0:
        last = x % 10
        x = x // 10
        if last < x % 10:
            return False
    return True
