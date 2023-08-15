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
        super().__init__(self, x, y, id)

    def __str__(self):
        """
        doc
        """
        return (f"[{self.__class__.__name__}] ({self.id})"
                f" {self.x}/{self.y} - {self.width}")
