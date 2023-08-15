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
        #super().__init__(id)

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
        self.__y = y
