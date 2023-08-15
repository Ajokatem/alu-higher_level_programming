#!/usr/bin/python3
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
        if not id
            __nb_objects += 1
            self.id = __nb_objects
        else:
            self.id = id
