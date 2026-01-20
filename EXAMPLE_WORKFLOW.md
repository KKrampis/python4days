# Example Workflow: Your First Exercise

This guide shows you **exactly** how to complete your first exercise and see the tests pass.

## Step 1: Run the Test (Before Implementation)

```bash
cd /home/user/python4days
python -m pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
```

**You'll see this (FAILING TEST):**
```
FAILED test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy

    def test_create_list_copy(self):
        original = [1, 2, 3]
        copied = create_list_copy(original)
>       copied.append(4)
        ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'append'
```

**Why it fails**: The function returns `None` (because of `pass`), so the test can't call `.append()` on it.

## Step 2: Look at the Function

Open `day1_morning_lists_tuples.py` and find:

```python
def create_list_copy(original):
    """
    Create a shallow copy of a list.

    Args:
        original: List to copy

    Returns:
        A shallow copy of the list

    Example:
        >>> original = [1, 2, 3]
        >>> copied = create_list_copy(original)
        >>> copied.append(4)
        >>> original
        [1, 2, 3]
    """
    # TODO: Implement shallow copy of the list
    # Hint: Use list.copy() or slicing
    pass
```

## Step 3: Implement the Function

Replace `pass` with your implementation:

```python
def create_list_copy(original):
    """
    Create a shallow copy of a list.
    ...
    """
    # TODO: Implement shallow copy of the list
    # Hint: Use list.copy() or slicing
    return original.copy()
```

**Alternative implementations that also work:**
```python
# Option 1: Using copy method
return original.copy()

# Option 2: Using slicing
return original[:]

# Option 3: Using list constructor
return list(original)
```

## Step 4: Save and Run Test Again

Save the file and run:

```bash
python -m pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
```

**You'll see this (PASSING TEST):**
```
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy PASSED [100%]

============================== 1 passed in 0.01s =============================
```

✅ **Success!** The test passes!

## Step 5: Run Related Tests

Now run all tests in that test class to make sure your implementation handles all cases:

```bash
python -m pytest test_day1_morning_lists_tuples.py::TestListFundamentals -v
```

**You'll see:**
```
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy PASSED
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy_empty PASSED
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_deep_copy FAILED
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_deep_copy_complex FAILED
```

The first two pass! Now implement `create_deep_copy` to make the others pass.

## Step 6: Continue to Next Function

Repeat the process:
1. Run the test for the next function
2. Read the error message
3. Implement the function
4. Run the test again
5. Iterate until it passes

## Using Zed Editor

### Split View Setup

1. Open `day1_morning_lists_tuples.py` in Zed
2. Press **Ctrl+K, then V** to split vertically
3. In the right pane, open `test_day1_morning_lists_tuples.py`
4. Now you can see both files side-by-side!

### Terminal in Zed

1. Press **Ctrl+`** to open terminal at the bottom
2. Run pytest commands in the terminal:
   ```bash
   python -m pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
   ```

### Your Workflow in Zed

```
┌─────────────────────────┬─────────────────────────┐
│ day1_morning_...py      │ test_day1_morning_...py │
│                         │                         │
│ def create_list_copy(   │ def test_create_list_   │
│     original):          │     copy(self):         │
│   # TODO: implement     │   original = [1, 2, 3]  │
│   return original.copy()│   copied = create_...   │
│                         │   assert ...            │
├─────────────────────────┴─────────────────────────┤
│ TERMINAL                                          │
│ $ pytest test_day1_morning_lists_tuples.py -v    │
│ PASSED ✓                                          │
└───────────────────────────────────────────────────┘
```

## Quick Reference: Essential Commands

```bash
# Install pytest (only needed once)
pip install pytest

# Run specific test
python -m pytest test_day1_morning_lists_tuples.py::TestClass::test_function -v

# Run all tests in a file
python -m pytest test_day1_morning_lists_tuples.py -v

# Run all Day 1 tests
python -m pytest -k "day1" -v

# Run all tests
python -m pytest -v

# Stop on first failure
python -m pytest -x

# Show print statements
python -m pytest -s
```

## Troubleshooting

### Issue: Import errors
**Solution**: Make sure you're in the project directory
```bash
cd /home/user/python4days
```

### Issue: pytest not found
**Solution**: Install it or use python -m
```bash
pip install pytest
# OR
python -m pytest -v
```

### Issue: All tests fail
**Solution**: This is expected! You haven't implemented the functions yet. Start with one function at a time.

## Progress Tracking

As you complete exercises, you can track your progress:

```bash
# See overall progress
python -m pytest --tb=no -q

# Example output:
# 5 passed, 23 failed in 0.50s
# This means you've completed 5 exercises!
```

## Next Steps

1. Complete all Day 1 Morning exercises
2. Move to Day 1 Afternoon
3. Continue through Days 2-4
4. Reference `python_coding_prep_days_1-4_comprehensive_guide.md` when stuck

**Good luck with your Python practice!** 🚀
