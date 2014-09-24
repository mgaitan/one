====================================
``one``, the missing Python function
====================================

.. image:: https://pypip.in/d/one/badge.png
        :target: https://pypi.python.org/pypi/one


Not ``all`` nor ``any``: just the ``one``.

``one`` is a simple function to check if there is a unique value
that evaluates to True in an iterable, and return it.

Examples:

.. code-block:: python

    >>> from one import one
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
    >>> one(('', 1))
    1

Install
--------

::

    pip install one



Use cases
----------

A very frequent case is when you have values that must exclude each others.


.. code-block:: python

    class ShopStore(models.Model):
        address = models.CharField(max_length=200, null=True, blank=True)
        is_online = models.BooleanField(default=False)

        def clean(self):
            if not one((self.address, self.is_online)):
                raise models.ValidationError(u'A shop must be online or physical, but not both')



        not all(iterable) or not any(iterable)



Send me your examples!


Performance
-----------

There are some performance comparissions in `this notebook <http://nbviewer.ipython.org/github/mgaitan/one/blob/master/testbenchs.ipynb>`_


