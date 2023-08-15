#!/usr/bin/python3
"""
module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        obj
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        doc
        """
        return (f"[{self.__class__.__name__}] ({self.id})"
                f" {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """
        doc
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        doc
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        updates all the attribute of a square
        """
        arg = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        elif kwargs:
            for attr in kwargs:
                setattr(self, attr, kwargs[attr])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        """
        return a dict repr of a square
        """
        a = self.__dict__
        my_dict = {}
        for key, value in a.items():
            if len(key) > 2:
                key = key[12:]
                if key in ["width", "height"]:
                    key = "size"
                my_dict[key] = value
            else:
                my_dict[key] = value
        return my_dict
