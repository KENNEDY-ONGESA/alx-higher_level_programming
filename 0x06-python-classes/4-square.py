#!/usr/bin/python3


class Square:
    """Square class."""

    def __init__(self, size=0):
        """__init__ method that sets the size of square.
        Args:
            size (int): size of Square
        """
        self.size = size

    def area(self):
        """Gets the area of the Square.
        Returns:
            Area of squre
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size setter  method that sets the size of square.
        Args:
            value (int): size of Square
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value