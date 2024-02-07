#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): The size of the new square
        """
        self.__size = size

        @property
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Returns the current area of the square"""
            return (self.__size * self.__size)
