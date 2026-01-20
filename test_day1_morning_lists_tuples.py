"""
Unit Tests for Day 1 Morning: Lists and Tuples
"""

import pytest
from day1_morning_lists_tuples import *


class TestListFundamentals:
    """Test list operations and performance understanding"""

    def test_create_list_copy(self):
        original = [1, 2, 3]
        copied = create_list_copy(original)
        copied.append(4)
        assert original == [1, 2, 3], "Original should not be modified"
        assert copied == [1, 2, 3, 4], "Copy should have new element"

    def test_create_list_copy_empty(self):
        assert create_list_copy([]) == []

    def test_create_deep_copy(self):
        original = [[1, 2], [3, 4]]
        deep = create_deep_copy(original)
        deep[0].append(3)
        assert original == [[1, 2], [3, 4]], "Original nested list should not change"
        assert deep == [[1, 2, 3], [3, 4]], "Deep copy should have new element"

    def test_create_deep_copy_complex(self):
        original = [[1, [2, 3]], [4, [5, 6]]]
        deep = create_deep_copy(original)
        deep[0][1].append(99)
        assert original[0][1] == [2, 3], "Original should not be affected"


class TestListComprehensions:
    """Test list comprehension patterns"""

    def test_squares_of_evens(self):
        assert squares_of_evens([1, 2, 3, 4, 5, 6]) == [4, 16, 36]

    def test_squares_of_evens_no_evens(self):
        assert squares_of_evens([1, 3, 5, 7]) == []

    def test_squares_of_evens_empty(self):
        assert squares_of_evens([]) == []

    def test_flatten_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert flatten_matrix(matrix) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_flatten_matrix_different_sizes(self):
        matrix = [[1, 2], [3, 4, 5], [6]]
        assert flatten_matrix(matrix) == [1, 2, 3, 4, 5, 6]

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        assert transpose_matrix(matrix) == expected

    def test_transpose_matrix_square(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        assert transpose_matrix(matrix) == expected


class TestAdvancedSlicing:
    """Test slicing operations"""

    def test_reverse_list(self):
        assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    def test_reverse_list_empty(self):
        assert reverse_list([]) == []

    def test_reverse_list_single(self):
        assert reverse_list([42]) == [42]

    def test_get_every_nth(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert get_every_nth(arr, 3) == [0, 3, 6, 9]

    def test_get_every_nth_two(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert get_every_nth(arr, 2) == [0, 2, 4, 6, 8]

    def test_rotate_list(self):
        assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    def test_rotate_list_full_rotation(self):
        arr = [1, 2, 3, 4, 5]
        assert rotate_list(arr, 5) == arr

    def test_rotate_list_larger_than_length(self):
        assert rotate_list([1, 2, 3], 7) == [2, 3, 1]  # 7 % 3 = 1


class TestTwoPointer:
    """Test two-pointer technique"""

    def test_two_sum_sorted(self):
        assert two_sum_sorted([1, 2, 3, 4, 5], 9) == [3, 4]

    def test_two_sum_sorted_first_last(self):
        assert two_sum_sorted([1, 2, 3, 4, 5], 6) == [0, 4]

    def test_two_sum_sorted_not_found(self):
        assert two_sum_sorted([1, 2, 3], 10) is None

    def test_two_sum_sorted_adjacent(self):
        assert two_sum_sorted([1, 2, 3, 4], 5) == [1, 2]

    def test_remove_duplicates_sorted(self):
        nums = [1, 1, 2, 2, 3, 4, 4]
        length = remove_duplicates_sorted(nums)
        assert length == 4
        assert nums[:length] == [1, 2, 3, 4]

    def test_remove_duplicates_sorted_no_dupes(self):
        nums = [1, 2, 3, 4]
        length = remove_duplicates_sorted(nums)
        assert length == 4
        assert nums[:length] == [1, 2, 3, 4]

    def test_remove_duplicates_sorted_all_same(self):
        nums = [1, 1, 1, 1]
        length = remove_duplicates_sorted(nums)
        assert length == 1

    def test_is_palindrome_list(self):
        assert is_palindrome_list([1, 2, 3, 2, 1]) is True

    def test_is_palindrome_list_even(self):
        assert is_palindrome_list([1, 2, 2, 1]) is True

    def test_is_palindrome_list_not(self):
        assert is_palindrome_list([1, 2, 3, 4]) is False

    def test_is_palindrome_list_empty(self):
        assert is_palindrome_list([]) is True

    def test_is_palindrome_list_single(self):
        assert is_palindrome_list([1]) is True


class TestTupleOperations:
    """Test tuple operations"""

    def test_swap_values(self):
        assert swap_values(10, 20) == (20, 10)

    def test_swap_values_different_types(self):
        assert swap_values("hello", 42) == (42, "hello")

    def test_unpack_first_last(self):
        assert unpack_first_last([1, 2, 3, 4, 5]) == (1, [2, 3, 4], 5)

    def test_unpack_first_last_two_elements(self):
        assert unpack_first_last([1, 2]) == (1, [], 2)

    def test_unpack_first_last_three_elements(self):
        assert unpack_first_last([1, 2, 3]) == (1, [2], 3)

    def test_create_point_namedtuple(self):
        Point = create_point_namedtuple()
        p = Point(10, 20)
        assert p.x == 10
        assert p.y == 20
        assert p[0] == 10
        assert p[1] == 20

    def test_get_min_max_avg(self):
        assert get_min_max_avg([1, 2, 3, 4, 5]) == (1, 5, 3.0)

    def test_get_min_max_avg_single(self):
        assert get_min_max_avg([42]) == (42, 42, 42.0)

    def test_get_min_max_avg_negatives(self):
        assert get_min_max_avg([-5, -1, 0, 3, 5]) == (-5, 5, 0.4)


class TestAdvancedListOperations:
    """Test advanced list manipulation"""

    def test_merge_sorted_lists(self):
        assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_sorted_lists_different_lengths(self):
        assert merge_sorted_lists([1, 5, 9], [2, 3, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7, 9]

    def test_merge_sorted_lists_one_empty(self):
        assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
        assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]

    def test_remove_element(self):
        nums = [3, 2, 2, 3, 4]
        length = remove_element(nums, 3)
        assert length == 3
        assert sorted(nums[:length]) == [2, 2, 4]

    def test_remove_element_all(self):
        nums = [1, 1, 1, 1]
        length = remove_element(nums, 1)
        assert length == 0

    def test_remove_element_none(self):
        nums = [1, 2, 3, 4]
        length = remove_element(nums, 5)
        assert length == 4

    def test_partition_list(self):
        nums = [3, 5, 1, 2, 4]
        idx = partition_list(nums, 3)
        # All elements before idx should be < 3
        assert all(x < 3 for x in nums[:idx])
        # All elements from idx onwards should be >= 3
        assert all(x >= 3 for x in nums[idx:])

    def test_partition_list_all_less(self):
        nums = [1, 2, 1, 2]
        idx = partition_list(nums, 10)
        assert idx == len(nums)

    def test_partition_list_all_greater(self):
        nums = [5, 6, 7, 8]
        idx = partition_list(nums, 3)
        assert idx == 0
