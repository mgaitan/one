def one(iterable):
    """Return the object in the given iterable that evaluates to True.

    If the given iterable has more than one object that evaluates to True,
    or if there is no object that fulfills such condition, return False.

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
    """
    iterable = iter(iterable)
    for item in iterable:
        if item:
            break
    else:
        return False
    if any(iterable):
        return False
    return item


if __name__ == "__main__":
    import doctest
    doctest.testmod()
