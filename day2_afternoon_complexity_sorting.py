"""
DAY 2 AFTERNOON: Algorithm Complexity and Sorting
==================================================

This module covers Big O notation, complexity analysis, and various sorting algorithms.

Topics:
- Big O complexity classes
- Complexity analysis principles
- Comparison-based sorting (insertion, merge, quick, heap)
- Non-comparison sorting (counting, radix)
- Binary search variations
"""


# ============================================================================
# SECTION 1: Basic Algorithms with Complexity Understanding
# ============================================================================

def binary_search(arr, target):
    """
    Binary search in sorted array - O(log n).

    Args:
        arr: Sorted list
        target: Value to find

    Returns:
        Index of target, or -1 if not found

    Example:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
    """
    # TODO: Implement binary search
    # Hint: Use two pointers left and right
    pass


def find_max(arr):
    """
    Find maximum element - O(n).

    Args:
        arr: List of numbers

    Returns:
        Maximum element

    Example:
        >>> find_max([3, 1, 4, 1, 5])
        5
    """
    # TODO: Iterate through array keeping track of max
    pass


# ============================================================================
# SECTION 2: Sorting Algorithms - Comparison-Based
# ============================================================================

def insertion_sort(arr):
    """
    Insertion sort - O(n²) worst case, O(n) best case.
    Stable, in-place, good for small or nearly sorted arrays.

    Args:
        arr: List to sort (modified in-place)

    Returns:
        Sorted list

    Example:
        >>> insertion_sort([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
    """
    # TODO: Implement insertion sort
    pass


def merge_sort(arr):
    """
    Merge sort - O(n log n) always.
    Stable, not in-place, reliable performance.

    Args:
        arr: List to sort

    Returns:
        Sorted list

    Example:
        >>> merge_sort([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
    """
    # TODO: Implement merge sort recursively
    pass


def quick_sort(arr):
    """
    Quick sort - O(n log n) average, O(n²) worst.
    Not stable, often fastest in practice.

    Args:
        arr: List to sort

    Returns:
        Sorted list

    Example:
        >>> quick_sort([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
    """
    # TODO: Implement quick sort
    pass


def bubble_sort(arr):
    """
    Bubble sort - O(n²).
    Stable, simple but inefficient.

    Args:
        arr: List to sort

    Returns:
        Sorted list

    Example:
        >>> bubble_sort([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
    """
    # TODO: Implement bubble sort
    pass


# ============================================================================
# SECTION 3: Non-Comparison Sorting
# ============================================================================

def counting_sort(arr, max_val=None):
    """
    Counting sort - O(n + k) where k is range.
    Stable, efficient when range is not much larger than n.

    Args:
        arr: List of non-negative integers
        max_val: Maximum value (if known)

    Returns:
        Sorted list

    Example:
        >>> counting_sort([3, 1, 4, 1, 5, 2])
        [1, 1, 2, 3, 4, 5]
    """
    # TODO: Implement counting sort
    pass


# ============================================================================
# SECTION 4: Binary Search Variations
# ============================================================================

def find_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array.

    Args:
        arr: Sorted list
        target: Value to find

    Returns:
        Index of first occurrence, or -1

    Example:
        >>> find_first_occurrence([1, 2, 2, 2, 3], 2)
        1
    """
    # TODO: Modified binary search - continue left even after finding
    pass


def find_last_occurrence(arr, target):
    """
    Find last occurrence of target in sorted array.

    Args:
        arr: Sorted list
        target: Value to find

    Returns:
        Index of last occurrence, or -1

    Example:
        >>> find_last_occurrence([1, 2, 2, 2, 3], 2)
        3
    """
    # TODO: Modified binary search - continue right even after finding
    pass


def search_rotated_array(arr, target):
    """
    Search in rotated sorted array.

    Args:
        arr: Rotated sorted array
        target: Value to find

    Returns:
        Index of target, or -1

    Example:
        >>> search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
    """
    # TODO: Modified binary search for rotated array
    pass


# ============================================================================
# SECTION 5: Complexity Analysis Helpers
# ============================================================================

def is_sorted(arr):
    """
    Check if array is sorted - O(n).

    Args:
        arr: List to check

    Returns:
        True if sorted in ascending order

    Example:
        >>> is_sorted([1, 2, 3, 4])
        True
    """
    # TODO: Check if each element <= next
    pass


def find_duplicates_linear(arr):
    """
    Find duplicates in O(n) time, O(n) space.

    Args:
        arr: List of integers

    Returns:
        Set of duplicate values

    Example:
        >>> find_duplicates_linear([1, 2, 3, 2, 4, 1])
        {1, 2}
    """
    # TODO: Use set to track seen elements
    pass
