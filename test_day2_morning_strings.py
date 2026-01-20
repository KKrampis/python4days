"""
Unit Tests for Day 2 Morning: String Manipulation
"""

import pytest
from day2_morning_strings import *


class TestStringMethods:
    def test_normalize_whitespace(self):
        assert normalize_whitespace('  hello   world  ') == 'hello world'
        assert normalize_whitespace('  test  ') == 'test'

    def test_title_case(self):
        assert title_case('hello world') == 'Hello World'
        assert title_case('python programming') == 'Python Programming'

    def test_swap_case(self):
        assert swap_case('Hello World') == 'hELLO wORLD'

    def test_count_vowels(self):
        assert count_vowels('Hello World') == 3
        assert count_vowels('AEIOU') == 5
        assert count_vowels('bcdfg') == 0


class TestSplittingJoining:
    def test_split_into_words(self):
        assert split_into_words('The quick brown fox') == ['The', 'quick', 'brown', 'fox']

    def test_split_csv_line(self):
        assert split_csv_line('apple,banana,cherry') == ['apple', 'banana', 'cherry']

    def test_join_with_separator(self):
        assert join_with_separator(['a', 'b', 'c'], '-') == 'a-b-c'

    def test_reverse_words(self):
        assert reverse_words('hello world python') == 'python world hello'


class TestFormatting:
    def test_format_person_info(self):
        result = format_person_info('Alice', 30, 'NYC')
        assert result == 'Alice is 30 years old and lives in NYC'

    def test_format_float(self):
        assert format_float(3.14159, 2) == '3.14'
        assert format_float(2.5, 1) == '2.5'

    def test_center_text(self):
        assert center_text('hello', 11) == '   hello   '


class TestRegex:
    def test_extract_numbers(self):
        assert extract_numbers('I have 2 apples and 15 oranges') == ['2', '15']

    def test_validate_email(self):
        assert validate_email('user@example.com') is True
        assert validate_email('invalid.email') is False

    def test_replace_multiple_spaces(self):
        assert replace_multiple_spaces('hello    world') == 'hello world'

    def test_find_hashtags(self):
        assert find_hashtags('Love #python and #coding!') == ['#python', '#coding']


class TestStringAlgorithms:
    def test_is_palindrome(self):
        assert is_palindrome('A man a plan a canal Panama') is True
        assert is_palindrome('hello') is False

    def test_are_anagrams(self):
        assert are_anagrams('listen', 'silent') is True
        assert are_anagrams('hello', 'world') is False

    def test_longest_unique_substring(self):
        assert longest_unique_substring('abcabcbb') == 3
        assert longest_unique_substring('bbbbb') == 1

    def test_compress_string(self):
        assert compress_string('aabbbcccc') == 'a2b3c4'
        assert compress_string('abc') == 'abc'

    def test_first_non_repeating_char(self):
        assert first_non_repeating_char('leetcode') == 'l'
        assert first_non_repeating_char('aabb') is None


class TestAdvancedOperations:
    def test_reverse_string(self):
        assert reverse_string('hello') == 'olleh'

    def test_is_rotation(self):
        assert is_rotation('waterbottle', 'erbottlewat') is True
        assert is_rotation('hello', 'world') is False

    def test_remove_duplicates_string(self):
        assert remove_duplicates_string('hello') == 'helo'

    def test_longest_common_prefix(self):
        assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
        assert longest_common_prefix(['dog', 'racecar', 'car']) == ''

    def test_count_words(self):
        assert count_words('hello world hello') == {'hello': 2, 'world': 1}
