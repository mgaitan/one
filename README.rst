====================================
``one``, the missing Python function
====================================

.. image:: https://pypip.in/d/one/badge.png
        :target: https://pypi.python.org/pypi/one

.. image:: https://travis-ci.org/mgaitan/one.svg
    :target: https://travis-ci.org/mgaitan/one


Not ``all`` nor ``any``: just the ``one``.

``one`` is a simple function to check if there is a unique value
that evaluates to True in an iterable, and return it. Optionally,
it receives a callable as the test function.

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
    >>> one((10, 20, 30, 42), lambda i: i > 40)
    42

Install & usage
---------------

Install it via pip::

   $ pip install one

.. code-block:: python

   from one import one

Since the version 0.6.3 ``one`` is also part of the wonderful library boltons_. So, alternatively
you can install that::

   $ pip install boltons

And import ``one``

.. code-block:: python

   from boltons.iterutils import one


.. _boltons: https://github.com/mahmoud/boltons



Patterns and use cases
----------------------

``one`` could replace the following patterns:

.. code-block:: python


        true_values = [i for i in iterable if cmp(i)]
        if len(true_values) == 1:
            return true_values[0]
        return False

        # using one
        return one(iterable, cmp)

Another pattern, is in a complex condition

.. code-block:: python


        if ((a and not b and not c) or
             (b and not a and not c) or
              (c and not a and not b)):
            do_something()

        # using one
        if one((a, b, c)):
            do_something()


A very frequent case is when you have values that must exclude each others.


.. code-block:: python

    class ShopStore(models.Model):
        address = models.CharField(max_length=200, null=True, blank=True)
        is_online = models.BooleanField(default=False)

        def clean(self):
            if not one((self.address, self.is_online)):
                raise models.ValidationError(u'A shop must be online or physical, but not both')


Send me your examples!