#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        creates sqr obj
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        initializes instance of a square
        Args:
            __size(int): size of square
            size must be positive and integer type
        """
