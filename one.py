def one(iterable):
    """
    Return X if X is the only one value where bool(i) is True for
    each every i in the iterable. In any other case return None.

    >>> one((True, False, False))
    True
    >>> one((True, False, True))
    False
    >>> one((0, 0, 'a'))
    'a'
    >>> one((0, False, None))
    False
    >>> bool(one((True, True)))
    False
    >>> bool(one((False, True)))
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