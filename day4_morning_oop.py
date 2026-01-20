"""
DAY 4 MORNING: Object-Oriented Programming
===========================================

This module covers classes, objects, inheritance, polymorphism,
encapsulation, and special methods.

Topics:
- Classes and objects
- Instance vs class attributes
- Methods (instance, class, static)
- Encapsulation and properties
- Inheritance and polymorphism
- Abstract base classes
- Special methods (magic methods)
"""

from abc import ABC, abstractmethod


# ============================================================================
# SECTION 1: Basic Classes
# ============================================================================

class Person:
    """
    Create a Person class with name and age attributes.

    Example:
        >>> p = Person('Alice', 30)
        >>> p.name
        'Alice'
        >>> p.greet()
        'Hello, I am Alice'
    """
    # TODO: Implement __init__, greet method, __str__, __repr__
    pass


class BankAccount:
    """
    Create a BankAccount class with encapsulation.

    Example:
        >>> acc = BankAccount('12345', 100)
        >>> acc.deposit(50)
        True
        >>> acc.balance
        150
    """
    # TODO: Implement __init__, deposit, withdraw, balance property
    pass


# ============================================================================
# SECTION 2: Class Methods and Static Methods
# ============================================================================

class Temperature:
    """
    Temperature class with multiple constructors.

    Example:
        >>> t = Temperature.from_fahrenheit(98.6)
        >>> t.celsius
        37.0
    """
    # TODO: Implement __init__, from_fahrenheit classmethod,
    # celsius/fahrenheit properties
    pass


class MathUtils:
    """
    Utility class with static methods.

    Example:
        >>> MathUtils.is_even(4)
        True
        >>> MathUtils.factorial(5)
        120
    """
    # TODO: Implement static methods is_even, factorial
    pass


# ============================================================================
# SECTION 3: Inheritance
# ============================================================================

class Animal:
    """Base animal class."""
    # TODO: Implement __init__ with name, make_sound (abstract)
    pass


class Dog(Animal):
    """Dog that inherits from Animal."""
    # TODO: Implement __init__ with breed, override make_sound
    pass


class Cat(Animal):
    """Cat that inherits from Animal."""
    # TODO: Override make_sound
    pass


# ============================================================================
# SECTION 4: Abstract Base Classes
# ============================================================================

class Shape(ABC):
    """Abstract shape class."""
    # TODO: Define abstract methods area and perimeter
    pass


class Rectangle(Shape):
    """Rectangle implementation of Shape."""
    # TODO: Implement area and perimeter
    pass


class Circle(Shape):
    """Circle implementation of Shape."""
    # TODO: Implement area and perimeter
    pass


# ============================================================================
# SECTION 5: Special Methods
# ============================================================================

class Vector:
    """
    2D Vector with operator overloading.

    Example:
        >>> v1 = Vector(1, 2)
        >>> v2 = Vector(3, 4)
        >>> v3 = v1 + v2
        >>> v3.x, v3.y
        (4, 6)
    """
    # TODO: Implement __init__, __repr__, __add__, __sub__,
    # __mul__ (scalar), __eq__, __abs__
    pass


class Stack:
    """
    Stack with special methods.

    Example:
        >>> s = Stack()
        >>> s.push(1)
        >>> s.push(2)
        >>> len(s)
        2
        >>> s.pop()
        2
    """
    # TODO: Implement push, pop, __len__, __bool__, __str__
    pass


# ============================================================================
# SECTION 6: Advanced OOP Patterns
# ============================================================================

class Counter:
    """
    Counter with context manager protocol.

    Example:
        >>> with Counter() as c:
        ...     c.increment()
        ...     c.count
        1
    """
    # TODO: Implement __init__, increment, __enter__, __exit__
    pass
