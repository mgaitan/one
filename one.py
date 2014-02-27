def one(iterable):
    """Return the object in the given iterable that evaluates to True.

    If the given iterable has more than one object that evaluates to True,
    or if there is no object that fulfills such condition, return None.

    >>> one((True, False, False))
    True
    >>> one((True, False, True))
    >>> one((0, 0, 'a'))
    'a'
    >>> one((0, False, None)) is None
    True
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
