"""
Unit Tests for Day 4 Afternoon: Problem-Solving Patterns
"""

import pytest
from day4_afternoon_patterns import *


class TestSlidingWindow:
    def test_max_sum_subarray(self):
        assert max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39

    def test_longest_substring_k_distinct(self):
        assert longest_substring_k_distinct('araaci', 2) == 4
        assert longest_substring_k_distinct('araaci', 1) == 2


class TestTwoPointers:
    def test_pair_with_target_sum(self):
        assert pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]

    def test_remove_duplicates(self):
        arr = [2, 3, 3, 3, 6, 9, 9]
        assert remove_duplicates(arr) == 4


class TestDynamicProgramming:
    def test_fibonacci_dp(self):
        assert fibonacci_dp(10) == 55
        assert fibonacci_dp(0) == 0

    def test_coin_change(self):
        assert coin_change([1, 2, 5], 11) == 3
        assert coin_change([2], 3) == -1

    def test_longest_increasing_subsequence(self):
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4


class TestBinarySearchPatterns:
    def test_search_insert_position(self):
        assert search_insert_position([1, 3, 5, 6], 5) == 2
        assert search_insert_position([1, 3, 5, 6], 2) == 1

    def test_find_peak_element(self):
        peak = find_peak_element([1, 2, 3, 1])
        assert peak == 2


class TestGraphTraversal:
    def test_bfs_traversal(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = bfs_traversal(graph, 1)
        assert result[0] == 1
        assert len(result) == 4

    def test_dfs_traversal(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = dfs_traversal(graph, 1)
        assert result[0] == 1

    def test_has_path(self):
        graph = {1: [2, 3], 2: [4], 3: [], 4: []}
        assert has_path(graph, 1, 4) is True
        assert has_path(graph, 3, 4) is False


class TestAdditionalPatterns:
    def test_find_all_duplicates(self):
        result = find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1])
        assert set(result) == {2, 3}

    def test_product_except_self(self):
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
