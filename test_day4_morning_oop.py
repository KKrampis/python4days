"""
Unit Tests for Day 4 Morning: Object-Oriented Programming
"""

import pytest
import math
from day4_morning_oop import *


class TestBasicClasses:
    def test_person(self):
        p = Person('Alice', 30)
        assert p.name == 'Alice'
        assert p.age == 30
        assert 'Alice' in p.greet()

    def test_bank_account(self):
        acc = BankAccount('12345', 100)
        acc.deposit(50)
        assert acc.balance == 150
        acc.withdraw(30)
        assert acc.balance == 120


class TestClassMethods:
    def test_temperature(self):
        t = Temperature.from_fahrenheit(98.6)
        assert abs(t.celsius - 37.0) < 0.1

    def test_math_utils(self):
        assert MathUtils.is_even(4) is True
        assert MathUtils.is_even(5) is False
        assert MathUtils.factorial(5) == 120


class TestInheritance:
    def test_dog(self):
        d = Dog('Rex', 'Labrador')
        assert d.name == 'Rex'
        assert 'Woof' in d.make_sound() or 'woof' in d.make_sound().lower()

    def test_cat(self):
        c = Cat('Whiskers')
        assert 'Meow' in c.make_sound() or 'meow' in c.make_sound().lower()


class TestAbstractClasses:
    def test_rectangle(self):
        r = Rectangle(4, 5)
        assert r.area() == 20
        assert r.perimeter() == 18

    def test_circle(self):
        c = Circle(5)
        assert abs(c.area() - math.pi * 25) < 0.01


class TestSpecialMethods:
    def test_vector_operations(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4 and v3.y == 6

    def test_stack(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert len(s) == 2
        assert s.pop() == 2


class TestAdvancedPatterns:
    def test_counter_context_manager(self):
        with Counter() as c:
            c.increment()
            assert c.count == 1
