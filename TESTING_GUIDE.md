# Testing Guide for Python 4-Day Prep

## Quick Start

### 1. Install pytest

First, ensure you have pytest installed:

```bash
pip install pytest
```

Or if you're using a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pytest
```

### 2. Run Tests

#### Run ALL tests:
```bash
pytest -v
```

#### Run tests for a specific day:
```bash
pytest -k "day1" -v
pytest -k "day2" -v
pytest -k "day3" -v
pytest -k "day4" -v
```

#### Run tests for a specific session:
```bash
pytest test_day1_morning_lists_tuples.py -v
pytest test_day1_afternoon_dicts_sets.py -v
pytest test_day2_morning_strings.py -v
pytest test_day2_afternoon_complexity_sorting.py -v
pytest test_day3_morning_functions.py -v
pytest test_day3_afternoon_recursion.py -v
pytest test_day4_morning_oop.py -v
pytest test_day4_afternoon_patterns.py -v
```

#### Run a specific test class:
```bash
pytest test_day1_morning_lists_tuples.py::TestListFundamentals -v
```

#### Run a specific test function:
```bash
pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
```

## Using Zed Editor

Zed has built-in Python support with testing capabilities. Here's how to use it effectively:

### Setting Up Python in Zed

1. **Open the project folder** in Zed:
   ```bash
   cd /home/user/python4days
   zed .
   ```

2. **Zed will automatically detect** Python files and activate Python language support

### Running Tests in Zed

#### Method 1: Using Zed's Terminal

1. Open the terminal in Zed: **Ctrl+`** (or **Cmd+`** on Mac)
2. Run pytest commands directly in the terminal:
   ```bash
   pytest -v
   ```

#### Method 2: Using Zed's Task Runner

1. Open Command Palette: **Ctrl+Shift+P** (or **Cmd+Shift+P** on Mac)
2. Type "Tasks: Spawn" and select it
3. Enter your pytest command

#### Method 3: Run Python File Directly (for quick testing)

1. Open a test file (e.g., `test_day1_morning_lists_tuples.py`)
2. Press **Ctrl+Shift+R** to run the current Python file
3. However, this runs the file directly, not through pytest

### Best Practice Workflow in Zed

1. **Split view**: Open exercise file on left, test file on right
   - **Ctrl+K, then V** to split vertically
   - Or use menu: View → Split

2. **Work on one function at a time**:
   - Find the TODO in the exercise file
   - Implement the function
   - Save the file (**Ctrl+S**)

3. **Run tests in terminal**:
   - Open terminal (**Ctrl+`**)
   - Run specific test:
     ```bash
     pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
     ```

4. **Iterate**:
   - If test fails, read the error message
   - Fix the implementation
   - Re-run the test

### Zed-Specific Python Configuration

Create a `.zed/settings.json` file in your project root for Python-specific settings:

```json
{
  "languages": {
    "Python": {
      "format_on_save": "on",
      "formatter": "black",
      "tab_size": 4
    }
  },
  "terminal": {
    "shell": {
      "program": "bash"
    }
  }
}
```

## Understanding Test Output

### When a test PASSES:
```
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy PASSED [100%]
```

### When a test FAILS:
```
test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy FAILED [100%]

______________________ TestListFundamentals.test_create_list_copy ______________________

    def test_create_list_copy(self):
        original = [1, 2, 3]
        copied = create_list_copy(original)
        copied.append(4)
>       assert original == [1, 2, 3], "Original should not be modified"
E       AssertionError: Original should not be modified
E       assert [1, 2, 3, 4] == [1, 2, 3]
```

This shows:
- **Where it failed**: In the assertion
- **What was expected**: `[1, 2, 3]`
- **What was actual**: `[1, 2, 3, 4]`
- **The error message**: "Original should not be modified"

## Useful pytest Options

```bash
# Verbose output with test names
pytest -v

# Stop on first failure
pytest -x

# Show local variables in tracebacks
pytest -l

# Run only failed tests from last run
pytest --lf

# Run tests matching a pattern
pytest -k "palindrome"

# Show print statements
pytest -s

# Coverage report (requires pytest-cov)
pip install pytest-cov
pytest --cov=. --cov-report=html
```

## Recommended Learning Workflow

1. **Start with Day 1 Morning**:
   ```bash
   pytest test_day1_morning_lists_tuples.py -v
   ```
   All tests will fail initially (that's expected!)

2. **Pick one test** that failed:
   ```bash
   pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
   ```

3. **Implement the function** in `day1_morning_lists_tuples.py`

4. **Re-run the specific test** until it passes

5. **Move to the next test**

6. **Run all tests for the session** to ensure nothing broke:
   ```bash
   pytest test_day1_morning_lists_tuples.py -v
   ```

7. **Reference the guide** (`python_coding_prep_days_1-4_comprehensive_guide.md`) if you get stuck

## Troubleshooting

### "pytest: command not found"
- Make sure pytest is installed: `pip install pytest`
- Or run: `python -m pytest -v`

### "ModuleNotFoundError"
- Make sure you're in the project directory: `cd /home/user/python4days`
- Check that the exercise file exists and is named correctly

### Tests pass but you used the guide's solution
- That's okay for learning! Try these next:
  1. Understand WHY the solution works
  2. Implement a variation or optimization
  3. Explain it as if teaching someone else
  4. Move to a similar but different problem

### Zed not detecting Python
- Ensure Python extension is enabled
- Check that Python is in your PATH: `which python` or `which python3`
- Restart Zed

## Additional Resources

- **pytest documentation**: https://docs.pytest.org/
- **Zed Python docs**: https://zed.dev/docs/languages/python
- **Python guide**: `python_coding_prep_days_1-4_comprehensive_guide.md` in this repo

Happy coding! 🐍
