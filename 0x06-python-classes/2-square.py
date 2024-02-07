#!/usr/bin/python3

"""Define a class called Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= to 0")
        self.__size = size
