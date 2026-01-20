"""
Unit Tests for Day 3 Afternoon: Recursion and Backtracking
"""

import pytest
from day3_afternoon_recursion import *


class TestBasicRecursion:
    def test_factorial(self):
        assert factorial(5) == 120
        assert factorial(0) == 1

    def test_fibonacci(self):
        assert fibonacci(6) == 8
        assert fibonacci(0) == 0

    def test_sum_list(self):
        assert sum_list([1, 2, 3, 4, 5]) == 15
        assert sum_list([]) == 0

    def test_reverse_string_recursive(self):
        assert reverse_string_recursive('hello') == 'olleh'


class TestMemoization:
    def test_fibonacci_memo(self):
        assert fibonacci_memo(50) == 12586269025


class TestTreeRecursion:
    def test_tree_height(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert tree_height(root) == 2
        assert tree_height(None) == 0

    def test_tree_sum(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert tree_sum(root) == 6

    def test_count_leaves(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert count_leaves(root) == 2


class TestBacktracking:
    def test_permutations(self):
        result = permutations([1, 2, 3])
        assert len(result) == 6
        assert [1, 2, 3] in result

    def test_combinations(self):
        result = combinations([1, 2, 3, 4], 2)
        assert len(result) == 6
        assert [1, 2] in result

    def test_subsets(self):
        result = subsets([1, 2, 3])
        assert len(result) == 8
        assert [] in result

    def test_generate_parentheses(self):
        result = generate_parentheses(3)
        assert len(result) == 5
        assert '((()))' in result

    def test_letter_combinations(self):
        result = letter_combinations('23')
        assert len(result) == 9
        assert 'ad' in result
