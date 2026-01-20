# Using This Repository with Zed Editor

Quick setup guide specifically for Zed editor users.

## 1. Open Project in Zed

```bash
cd /home/user/python4days
zed .
```

## 2. Install Python Dependencies

Open Zed's terminal (**Ctrl+`** or **Cmd+`**) and run:

```bash
pip install pytest
```

## 3. Recommended Zed Configuration

Create `.zed/settings.json` in the project root:

```json
{
  "languages": {
    "Python": {
      "format_on_save": "on",
      "tab_size": 4,
      "hard_tabs": false
    }
  },
  "terminal": {
    "shell": {
      "program": "bash"
    },
    "working_directory": "current_project_directory"
  },
  "vim_mode": false
}
```

## 4. Optimal Layout for Practice

### Setup Split View:

1. Open an exercise file (e.g., `day1_morning_lists_tuples.py`)
2. Press **Ctrl+K**, then **V** (or **Cmd+K, V** on Mac) to split vertically
3. In the right pane, open the corresponding test file (`test_day1_morning_lists_tuples.py`)
4. Press **Ctrl+`** to open terminal at the bottom

Your screen should look like:

```
┌─────────────────────────┬─────────────────────────┐
│                         │                         │
│  Exercise File          │  Test File              │
│  (Implement here)       │  (See what to pass)     │
│                         │                         │
│                         │                         │
│                         │                         │
│                         │                         │
│                         │                         │
├─────────────────────────┴─────────────────────────┤
│  Terminal (Run tests here)                        │
│  $ pytest test_day1_morning_lists_tuples.py -v    │
└───────────────────────────────────────────────────┘
```

## 5. Essential Zed Keyboard Shortcuts

| Action                    | Shortcut (Linux/Windows) | Shortcut (Mac)    |
|---------------------------|--------------------------|-------------------|
| Open Command Palette      | Ctrl+Shift+P             | Cmd+Shift+P       |
| Open Terminal             | Ctrl+`                   | Cmd+`             |
| Split Vertically          | Ctrl+K, V                | Cmd+K, V          |
| Split Horizontally        | Ctrl+K, S                | Cmd+K, S          |
| Focus Next Pane           | Ctrl+K, Ctrl+→           | Cmd+K, Cmd+→      |
| Focus Previous Pane       | Ctrl+K, Ctrl+←           | Cmd+K, Cmd+←      |
| Close Pane                | Ctrl+W                   | Cmd+W             |
| Save File                 | Ctrl+S                   | Cmd+S             |
| Go to File                | Ctrl+P                   | Cmd+P             |
| Search in Files           | Ctrl+Shift+F             | Cmd+Shift+F       |
| Find in File              | Ctrl+F                   | Cmd+F             |

## 6. Workflow Example

### Step-by-Step Process:

1. **Open files**:
   - Left: `day1_morning_lists_tuples.py`
   - Right: `test_day1_morning_lists_tuples.py`

2. **In test file**, find a test you want to pass:
   ```python
   def test_create_list_copy(self):
       original = [1, 2, 3]
       copied = create_list_copy(original)
       # ...
   ```

3. **In exercise file**, find the corresponding function:
   ```python
   def create_list_copy(original):
       # TODO: Implement shallow copy of the list
       pass
   ```

4. **Implement the function**:
   ```python
   def create_list_copy(original):
       # TODO: Implement shallow copy of the list
       return original.copy()
   ```

5. **Save**: Press **Ctrl+S**

6. **In terminal**, run the test:
   ```bash
   pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v
   ```

7. **See it pass!** ✅

## 7. Running Tests in Zed

### Method 1: Using Integrated Terminal (Recommended)

Open terminal with **Ctrl+`** and run:

```bash
# Single test
pytest test_day1_morning_lists_tuples.py::TestListFundamentals::test_create_list_copy -v

# All tests in a file
pytest test_day1_morning_lists_tuples.py -v

# All tests for a day
pytest -k "day1" -v

# All tests
pytest -v
```

### Method 2: Using Command Palette

1. Press **Ctrl+Shift+P**
2. Type "Tasks: Spawn"
3. Enter: `pytest test_day1_morning_lists_tuples.py -v`

## 8. Tips for Effective Learning in Zed

### Tip 1: Use Split Panes
- Keep exercise file on left, test file on right
- Quickly see what tests expect while coding

### Tip 2: Terminal at Bottom
- Run tests immediately after saving
- See results without switching windows

### Tip 3: Use Go to Symbol
- Press **Ctrl+Shift+O** to see all functions in current file
- Quickly jump between functions

### Tip 4: Search Across Files
- **Ctrl+Shift+F** to search all files
- Useful for finding similar patterns in the guide

### Tip 5: Multiple Terminals
- Open multiple terminal tabs for different tasks
- One for running tests, one for checking docs

## 9. Troubleshooting in Zed

### Python Not Found
- Ensure Python is installed: `python --version` or `python3 --version`
- Zed should auto-detect Python

### Tests Not Running
- Make sure you're in the project directory
- Check terminal working directory: `pwd`
- Should show: `/home/user/python4days`

### Import Errors
- Ensure you're running tests from project root
- In terminal: `cd /home/user/python4days`

### Zed Not Showing Errors
- Python LSP should be enabled by default
- Check: Command Palette → "zed: open settings"
- Ensure Python support is enabled

## 10. Advanced: Custom Tasks in Zed

Create `.zed/tasks.json` for quick test running:

```json
[
  {
    "label": "Run All Tests",
    "command": "pytest",
    "args": ["-v"]
  },
  {
    "label": "Run Day 1 Tests",
    "command": "pytest",
    "args": ["-k", "day1", "-v"]
  },
  {
    "label": "Run Current Test File",
    "command": "pytest",
    "args": ["${file}", "-v"]
  }
]
```

Then access via: **Ctrl+Shift+P** → "Tasks: ..."

## Quick Command Reference

```bash
# First time setup
pip install pytest

# Run tests (in Zed terminal)
pytest -v                           # All tests
pytest -k "day1" -v                # Day 1 only
pytest test_day1_morning_*.py -v   # Specific file
pytest -x                          # Stop on first fail
pytest -s                          # Show print output
```

## Getting Started Now!

1. Open Zed: `zed /home/user/python4days`
2. Split view: **Ctrl+K, V**
3. Open terminal: **Ctrl+`**
4. Start coding: Open `day1_morning_lists_tuples.py`
5. Run tests: `pytest test_day1_morning_lists_tuples.py -v`

**Happy coding!** 🎯
