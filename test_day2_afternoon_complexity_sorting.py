"""
Unit Tests for Day 2 Afternoon: Algorithm Complexity and Sorting
"""

import pytest
from day2_afternoon_complexity_sorting import *


class TestBasicAlgorithms:
    def test_binary_search(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2
        assert binary_search([1, 2, 3, 4, 5], 6) == -1

    def test_find_max(self):
        assert find_max([3, 1, 4, 1, 5]) == 5
        assert find_max([1]) == 1


class TestSortingAlgorithms:
    def test_insertion_sort(self):
        assert insertion_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert insertion_sort([]) == []

    def test_merge_sort(self):
        assert merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_quick_sort(self):
        assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert quick_sort([1]) == [1]

    def test_bubble_sort(self):
        assert bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


class TestNonComparisonSorting:
    def test_counting_sort(self):
        assert counting_sort([3, 1, 4, 1, 5, 2]) == [1, 1, 2, 3, 4, 5]
        assert counting_sort([0, 0, 0]) == [0, 0, 0]


class TestBinarySearchVariations:
    def test_find_first_occurrence(self):
        assert find_first_occurrence([1, 2, 2, 2, 3], 2) == 1

    def test_find_last_occurrence(self):
        assert find_last_occurrence([1, 2, 2, 2, 3], 2) == 3

    def test_search_rotated_array(self):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1


class TestComplexityAnalysis:
    def test_is_sorted(self):
        assert is_sorted([1, 2, 3, 4]) is True
        assert is_sorted([1, 3, 2, 4]) is False

    def test_find_duplicates_linear(self):
        assert find_duplicates_linear([1, 2, 3, 2, 4, 1]) == {1, 2}
        assert find_duplicates_linear([1, 2, 3]) == set()
