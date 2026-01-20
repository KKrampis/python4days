"""
DAY 3 AFTERNOON: Recursion and Backtracking
============================================

This module covers recursive thinking, tree recursion, memoization,
and backtracking patterns.

Topics:
- Basic recursion
- Recursion with memoization
- Tree recursion
- Backtracking template
- Permutations and combinations
- Classic backtracking problems
"""


# ============================================================================
# SECTION 1: Basic Recursion
# ============================================================================

def factorial(n):
    """
    Calculate factorial recursively.

    Args:
        n: Non-negative integer

    Returns:
        n!

    Example:
        >>> factorial(5)
        120
    """
    # TODO: Base case n == 0, recursive case n * factorial(n-1)
    pass


def fibonacci(n):
    """
    Calculate nth Fibonacci number recursively.

    Args:
        n: Non-negative integer

    Returns:
        nth Fibonacci number

    Example:
        >>> fibonacci(6)
        8
    """
    # TODO: Base cases n <= 1, recursive case
    pass


def sum_list(numbers):
    """
    Sum list recursively.

    Args:
        numbers: List of numbers

    Returns:
        Sum of all numbers

    Example:
        >>> sum_list([1, 2, 3, 4, 5])
        15
    """
    # TODO: Base case empty list, recursive case first + sum(rest)
    pass


def reverse_string_recursive(s):
    """
    Reverse string recursively.

    Args:
        s: String to reverse

    Returns:
        Reversed string

    Example:
        >>> reverse_string_recursive('hello')
        'olleh'
    """
    # TODO: Base case len <= 1, recursive case last + reverse(rest)
    pass


# ============================================================================
# SECTION 2: Recursion with Memoization
# ============================================================================

def fibonacci_memo(n, memo=None):
    """
    Fibonacci with memoization for O(n) time.

    Args:
        n: Non-negative integer
        memo: Cache dictionary

    Returns:
        nth Fibonacci number

    Example:
        >>> fibonacci_memo(50)
        12586269025
    """
    # TODO: Use memo dict to cache results
    pass


# ============================================================================
# SECTION 3: Tree Recursion
# ============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_height(root):
    """
    Calculate height of binary tree.

    Args:
        root: TreeNode or None

    Returns:
        Height of tree

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> tree_height(root)
        2
    """
    # TODO: Base case None returns 0, recursive case 1 + max(left, right)
    pass


def tree_sum(root):
    """
    Sum all values in tree.

    Args:
        root: TreeNode or None

    Returns:
        Sum of all node values

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> tree_sum(root)
        6
    """
    # TODO: Base case None returns 0, recursive case
    pass


def count_leaves(root):
    """
    Count leaf nodes in tree.

    Args:
        root: TreeNode or None

    Returns:
        Number of leaf nodes

    Example:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> count_leaves(root)
        2
    """
    # TODO: Leaf is node with no children
    pass


# ============================================================================
# SECTION 4: Backtracking - Permutations and Combinations
# ============================================================================

def permutations(nums):
    """
    Generate all permutations.

    Args:
        nums: List of unique integers

    Returns:
        List of all permutations

    Example:
        >>> permutations([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    # TODO: Use backtracking with choose/explore/unchoose pattern
    pass


def combinations(nums, k):
    """
    Generate all k-element combinations.

    Args:
        nums: List of unique integers
        k: Combination size

    Returns:
        List of all k-element combinations

    Example:
        >>> combinations([1, 2, 3, 4], 2)
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    # TODO: Backtracking starting from different positions
    pass


def subsets(nums):
    """
    Generate all subsets (power set).

    Args:
        nums: List of unique integers

    Returns:
        List of all subsets

    Example:
        >>> subsets([1, 2, 3])
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    # TODO: Backtracking that includes empty set
    pass


# ============================================================================
# SECTION 5: Classic Backtracking Problems
# ============================================================================

def generate_parentheses(n):
    """
    Generate all valid combinations of n pairs of parentheses.

    Args:
        n: Number of pairs

    Returns:
        List of valid combinations

    Example:
        >>> generate_parentheses(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    # TODO: Track open and close counts, backtrack when valid
    pass


def letter_combinations(digits):
    """
    Letter combinations of phone number.

    Args:
        digits: String of digits 2-9

    Returns:
        List of letter combinations

    Example:
        >>> letter_combinations('23')
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """
    # TODO: Map digits to letters, backtrack through combinations
    pass
