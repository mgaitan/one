from __future__ import print_function   # noqa


def one(iterable, cmp=None):
    """
    Return the object in the given iterable that evaluates to True.

    If the given iterable has more than one object that evaluates to True,
    or if there is no object that fulfills such condition, return False.

    If a callable ``cmp`` is given, it's used to evaluate each element.


        >>> one((True, False, False))
        True
        >>> one((True, False, True))
        False
        >>> one((0, 0, 'a'))
        'a'
        >>> one((0, False, None))
        False
        >>> one((True, True))
        False
        >>> bool(one(('', 1)))
        True
        >>> one((10, 20, 30, 42), lambda i: i > 40)
        42
    """
    the_one = False
    for i in iterable:
        if cmp(i) if cmp else i:
            if the_one:
                return False
            the_one = i
    return the_one


def test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number=100))
