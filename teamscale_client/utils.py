import json
from typing import Any, Dict


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


def to_json(obj: Any) -> str:
    """Utility method for converting an object to a json encoded string.
    
    Args:
        obj: The object that should be encoded.
        
    Returns:
        str: The encoded version of the given object.
    """
    return json.dumps(obj, sort_keys=True, default=lambda x: vars(x))


def to_dict(obj: Any) -> Dict:
    """Utility method for converting any (nested!) object to a dict. This can be conveniently modified and e.g.
    given to the json parameters of a requests call.

    Args:
        obj: The object that should be encoded.

    Returns:
        dict: The dict version of the given object.
    """
    return json.loads(to_json(obj))
