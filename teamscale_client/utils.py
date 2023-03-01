from typing import Dict

import jsonpickle
from jsonpickle.pickler import Pickler


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


def to_json(obj):
    """Utility method for converting an object to a json encoded string. 
    
    Takes care of all the necessary setup.
    
    Args:
        obj (object): The object that should be encoded.
        
    Returns:
        str: The encoded version of the given object.
    """
    jsonpickle.set_encoder_options('simplejson', sort_keys=True)
    return jsonpickle.encode(obj, unpicklable=False)


def to_json_dict(obj: any) -> Dict:
    """Converts any object to a JSON dictionary which can be sent as payload of a request.

    Args:
        obj: the object to convert to a dictionary

    Returns:
        dictionary of the obj

    """
    pickler = Pickler(unpicklable=True)
    return pickler.flatten(obj)
