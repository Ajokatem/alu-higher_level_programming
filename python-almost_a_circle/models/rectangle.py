#!/usr/bin/python3
"""
my module
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intantinting obj
        """
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(id)
