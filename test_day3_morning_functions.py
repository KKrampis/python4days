"""
Unit Tests for Day 3 Morning: Functions and Higher-Order Programming
"""

import pytest
from day3_morning_functions import *


class TestFunctionBasics:
    def test_apply_operation(self):
        assert apply_operation(lambda x: x * 2, 5) == 10

    def test_create_operation_dict(self):
        ops = create_operation_dict()
        assert ops['square'](4) == 16
        assert ops['double'](5) == 10


class TestAdvancedParameters:
    def test_flexible_sum(self):
        assert flexible_sum(1, 2, 3, 4, 5) == 15
        assert flexible_sum(10) == 10

    def test_build_profile(self):
        result = build_profile(name='Alice', age=30, city='NYC')
        assert result == {'name': 'Alice', 'age': 30, 'city': 'NYC'}

    def test_mixed_parameters(self):
        result = mixed_parameters(1, 2, 3, 4, keyword_only=5, extra=6)
        assert 'pos' in result
        assert 'args' in result


class TestClosures:
    def test_make_multiplier(self):
        times_3 = make_multiplier(3)
        assert times_3(4) == 12

    def test_make_counter(self):
        counter = make_counter(10)
        assert counter() == 11
        assert counter() == 12


class TestDecorators:
    def test_uppercase_decorator(self):
        @uppercase_decorator
        def greet(name):
            return f"hello {name}"
        assert greet("world") == "HELLO WORLD"

    def test_repeat_decorator(self):
        @repeat_decorator(3)
        def say_hello():
            return "Hello"
        assert say_hello() == ["Hello", "Hello", "Hello"]

    def test_memoize(self):
        @memoize
        def fib(n):
            return n if n < 2 else fib(n-1) + fib(n-2)
        assert fib(10) == 55


class TestHigherOrderFunctions:
    def test_use_map(self):
        assert use_map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]

    def test_use_filter(self):
        assert use_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]

    def test_use_reduce(self):
        assert use_reduce(lambda x, y: x + y, [1, 2, 3, 4]) == 10

    def test_compose(self):
        add_10 = lambda x: x + 10
        double = lambda x: x * 2
        f = compose(add_10, double)
        assert f(5) == 20

    def test_pipeline(self):
        f = pipeline(lambda x: x + 1, lambda x: x * 2, lambda x: x - 3)
        assert f(5) == 9

    def test_create_partial(self):
        def power(base, exp):
            return base ** exp
        square = create_partial(power, exp=2)
        assert square(5) == 25
