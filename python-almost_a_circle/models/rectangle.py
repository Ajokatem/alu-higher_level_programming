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
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """
        doc
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        doc
        """
        if not isinstance(width, int):
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def width(self):
        """
        doc
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        doc
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def x(self):
        """
        doc
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        doc
        """
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        doc
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        doc
        """
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
