
def one(iterable):
    """
    Return X if X is the only one value where bool(i) is True for
    each every i in the iterable. In any other case return None.

    >>> one((True, False, False))
    True
    >>> one((True, False, True))
    >>> one((0, 0, 'a'))
    'a'
    >>> one((0, False, None))
    >>> bool(one((True, True)))
    False
    >>> bool(one((False, True)))
    True
    """
    the_one = None
    for i in iterable:
        if i:
            if the_one:
                return None
            the_one = i
    return the_one


if __name__ == "__main__":
    import doctest
    doctest.testmod()
