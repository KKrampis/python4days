"""
Unit Tests for Day 1 Afternoon: Dictionaries and Sets
"""

import pytest
from collections import Counter
from day1_afternoon_dicts_sets import *


class TestDictFundamentals:
    """Test dictionary operations"""

    def test_create_dict_from_lists(self):
        result = create_dict_from_lists(['a', 'b', 'c'], [1, 2, 3])
        assert result == {'a': 1, 'b': 2, 'c': 3}

    def test_create_dict_from_lists_empty(self):
        assert create_dict_from_lists([], []) == {}

    def test_invert_dict(self):
        assert invert_dict({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}

    def test_invert_dict_empty(self):
        assert invert_dict({}) == {}

    def test_merge_dicts(self):
        result = merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        assert result == {'a': 1, 'b': 3, 'c': 4}

    def test_merge_dicts_no_overlap(self):
        result = merge_dicts({'a': 1}, {'b': 2})
        assert result == {'a': 1, 'b': 2}

    def test_filter_dict_by_value(self):
        result = filter_dict_by_value({'a': 1, 'b': 5, 'c': 3}, 2)
        assert result == {'b': 5, 'c': 3}

    def test_filter_dict_by_value_all_pass(self):
        result = filter_dict_by_value({'a': 5, 'b': 6}, 2)
        assert result == {'a': 5, 'b': 6}

    def test_filter_dict_by_value_none_pass(self):
        result = filter_dict_by_value({'a': 1, 'b': 2}, 10)
        assert result == {}


class TestDefaultDictPatterns:
    """Test defaultdict patterns"""

    def test_group_by_length(self):
        result = group_by_length(['a', 'bb', 'ccc', 'dd'])
        assert result == {1: ['a'], 2: ['bb', 'dd'], 3: ['ccc']}

    def test_group_by_length_empty(self):
        assert group_by_length([]) == {}

    def test_count_characters(self):
        result = count_characters('hello')
        assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    def test_count_characters_repeated(self):
        result = count_characters('aaa')
        assert result == {'a': 3}

    def test_build_adjacency_list(self):
        result = build_adjacency_list([(1, 2), (1, 3), (2, 3)])
        assert result == {1: [2, 3], 2: [3]}

    def test_build_adjacency_list_empty(self):
        assert build_adjacency_list([]) == {}

    def test_build_adjacency_list_cycle(self):
        result = build_adjacency_list([(1, 2), (2, 3), (3, 1)])
        assert result == {1: [2], 2: [3], 3: [1]}


class TestCounterOperations:
    """Test Counter operations"""

    def test_most_common_elements(self):
        result = most_common_elements(['a', 'b', 'a', 'c', 'a', 'b'], 2)
        assert result == [('a', 3), ('b', 2)]

    def test_most_common_elements_single(self):
        result = most_common_elements(['x', 'x', 'y'], 1)
        assert result == [('x', 2)]

    def test_char_frequency(self):
        freq = char_frequency('hello')
        assert freq['l'] == 2
        assert freq['h'] == 1

    def test_char_frequency_counter_type(self):
        freq = char_frequency('test')
        assert isinstance(freq, Counter)

    def test_find_anagram_groups(self):
        result = find_anagram_groups(['eat', 'tea', 'tan', 'ate', 'nat'])
        # Sort for comparison since order may vary
        result_sorted = [sorted(group) for group in result]
        expected_sorted = [sorted(group) for group in [['eat', 'tea', 'ate'], ['tan', 'nat']]]
        assert sorted(result_sorted) == sorted(expected_sorted)


class TestSetOperations:
    """Test set operations"""

    def test_set_union(self):
        assert set_union({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}

    def test_set_union_disjoint(self):
        assert set_union({1, 2}, {3, 4}) == {1, 2, 3, 4}

    def test_set_intersection(self):
        assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

    def test_set_intersection_empty(self):
        assert set_intersection({1, 2}, {3, 4}) == set()

    def test_set_difference(self):
        assert set_difference({1, 2, 3}, {2, 3, 4}) == {1}

    def test_set_difference_all_removed(self):
        assert set_difference({1, 2}, {1, 2, 3}) == set()

    def test_symmetric_difference(self):
        assert symmetric_difference({1, 2, 3}, {2, 3, 4}) == {1, 4}

    def test_symmetric_difference_disjoint(self):
        assert symmetric_difference({1, 2}, {3, 4}) == {1, 2, 3, 4}


class TestCommonPatterns:
    """Test common dict/set patterns"""

    def test_remove_duplicates(self):
        assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]

    def test_remove_duplicates_no_dupes(self):
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_remove_duplicates_empty(self):
        assert remove_duplicates([]) == []

    def test_find_missing_number(self):
        assert find_missing_number([0, 1, 3]) == 2

    def test_find_missing_number_zero(self):
        assert find_missing_number([1, 2, 3]) == 0

    def test_find_missing_number_last(self):
        assert find_missing_number([0, 1, 2]) == 3

    def test_find_duplicates(self):
        assert find_duplicates([1, 2, 3, 2, 4, 1]) == {1, 2}

    def test_find_duplicates_none(self):
        assert find_duplicates([1, 2, 3, 4]) == set()

    def test_common_elements(self):
        assert common_elements([1, 2, 3], [2, 3, 4], [2, 5, 3]) == {2, 3}

    def test_common_elements_none(self):
        assert common_elements([1, 2], [3, 4], [5, 6]) == set()

    def test_is_subset(self):
        assert is_subset({1, 2}, {1, 2, 3, 4}) is True

    def test_is_subset_not(self):
        assert is_subset({1, 5}, {1, 2, 3, 4}) is False

    def test_is_subset_equal(self):
        assert is_subset({1, 2}, {1, 2}) is True


class TestAdvancedProblems:
    """Test advanced dictionary/set problems"""

    def test_two_sum(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_two_sum_different_order(self):
        result = two_sum([3, 2, 4], 6)
        assert result == [1, 2]

    def test_two_sum_not_found(self):
        assert two_sum([1, 2, 3], 10) is None

    def test_first_unique_char(self):
        assert first_unique_char('leetcode') == 0

    def test_first_unique_char_middle(self):
        assert first_unique_char('loveleetcode') == 2

    def test_first_unique_char_none(self):
        assert first_unique_char('aabbcc') == -1

    def test_group_anagrams(self):
        result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        # Sort for comparison
        result_sorted = [sorted(group) for group in result]
        expected = [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
        expected_sorted = [sorted(group) for group in expected]
        assert sorted(result_sorted) == sorted(expected_sorted)

    def test_longest_consecutive_sequence(self):
        assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4

    def test_longest_consecutive_sequence_single(self):
        assert longest_consecutive_sequence([1]) == 1

    def test_longest_consecutive_sequence_none(self):
        assert longest_consecutive_sequence([]) == 0

    def test_has_duplicate(self):
        assert has_duplicate([1, 2, 3, 1]) is True

    def test_has_duplicate_none(self):
        assert has_duplicate([1, 2, 3, 4]) is False

    def test_intersection_of_arrays(self):
        result = intersection_of_arrays([1, 2, 3], [2, 3, 4], [2, 3, 5])
        assert result == {2, 3}

    def test_intersection_of_arrays_two(self):
        result = intersection_of_arrays([1, 2, 3], [2, 3, 4])
        assert result == {2, 3}

    def test_intersection_of_arrays_single(self):
        result = intersection_of_arrays([1, 2, 3])
        assert result == {1, 2, 3}
