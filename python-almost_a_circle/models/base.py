#!/bin/python3
"""
module
"""


class Base():
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        intantiating a new obj
        """
        if id is None:
            __nb_objects += 1
            self.id = __nb_objects
        else:
            self.id = id
