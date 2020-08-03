def auto_str(cls):
    """Annotation that provides a default __str__ method for objects.

    Example:
        Annotating a class with the ``@auto_str`` annotation::

            >>> @auto_str
                class Dummy(object):
                    def __init__(self, a):
                        self.a = a

            >>> sample = Dummy("test")
            >>> print(sample)
            Dummy(a=test)
    """

    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls
