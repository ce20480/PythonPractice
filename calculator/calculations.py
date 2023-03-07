# calculator/calculations.py
"""
Module Docstring at start of file 

Example Google-Style Python Docstrings

This is a lnger description of the module. It can span multiple lines.

Args:
    param1 (int): The first parameter.
    param2 (str): The second parameter.

Returns:
    bool: The return value. True for success, False otherwise.

Raises:
    KeyError: Raises an exception.

--------------------
Docstring is used for:

Usage Instructions
Functions
Classes
Modules
"""


def add(x: float | int, y: float | int) -> float:
    """Add 2 numbers

    Examples:
        >>> add(1, 2)
        3
        >>> add(1, 2.5)
        3.5

    Args:
        x (float): First number
        y (float): Second number
    Returns:
        float: The sum of x and y
    """
    return float(x + y)


def subtract(x: float | int, y: float | int) -> float:
    """Subtract 2 numbers

    Examples:
        >>> subtract(1, 2)
        -1
        >>> subtract(1, 2.5)
        -1.5

    Args:
        x (float): First number
        y (float): Second number
    Returns:
        float: The sum of x and y
    """
    return float(x - y)


def multiply(x: float | int, y: float | int) -> float:
    """Multiply 2 numbers

    Examples:
        >>> multiply(1, 2)
        2
        >>> multiply(1, 2.5)
        2.5

    Args:
        x (float): First number
        y (float): Second number
    Returns:
        float: The sum of x and y
    """
    return float(x * y)


def divide(x: float | int, y: float | int) -> float | None:
    """Divide 2 numbers

    Examples:
        >>> divide(1, 2)
        0.5
        >>> divide(1, 2.5)
        0.4

    Args:
        x (float): First number
        y (float): Second number
    Returns:
        float: The sum of x and y
    Raises:
        ZeroDivisionError: If y is 0
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return float(x / y)
