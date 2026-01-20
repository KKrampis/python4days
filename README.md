# Python 4-Day Coding Test Preparation

## 🚀 Quick Start

**New to this repository?** Start here:
- **Using Zed Editor?** → Read [ZED_SETUP.md](ZED_SETUP.md)
- **First time running tests?** → Read [EXAMPLE_WORKFLOW.md](EXAMPLE_WORKFLOW.md)
- **Need help with pytest?** → Read [TESTING_GUIDE.md](TESTING_GUIDE.md)

## Overview

This repository is a comprehensive Python programming practice workspace created by **Claude Code** to help developers prepare intensively for coding interviews and technical assessments. The entire codebase was generated from the comprehensive guide `python_coding_prep_days_1-4_comprehensive_guide.md`, which was also created by Claude.

## Repository Structure

The repository is organized into **8 sessions** (4 days × 2 sessions per day), each covering different aspects of Python programming:

### Day 1: Data Structures Fundamentals
- **Morning Session**: Lists and Tuples - Deep Dive
- **Afternoon Session**: Dictionaries and Sets

### Day 2: Strings and Algorithms
- **Morning Session**: String Manipulation and Patterns
- **Afternoon Session**: Algorithm Complexity and Sorting

### Day 3: Functional and Recursive Programming
- **Morning Session**: Functions and Higher-Order Programming
- **Afternoon Session**: Recursion and Backtracking

### Day 4: OOP and Problem-Solving Patterns
- **Morning Session**: Object-Oriented Programming
- **Afternoon Session**: Problem-Solving Patterns

## How It Works

### Exercise Files
Each session has a corresponding Python file (e.g., `day1_morning_lists_tuples.py`) containing:
- **Skeleton functions** with `TODO` comments indicating where you need to write code
- **Docstrings** explaining what each function should do
- **Example usage** in comments to guide your implementation

### Unit Tests
Each exercise file has a matching test file (e.g., `test_day1_morning_lists_tuples.py`) containing:
- **Comprehensive unit tests** for all exercises
- **Multiple test cases** covering edge cases and typical scenarios
- **Immediate feedback** when you run the tests

### Practice Workflow

1. **Choose a session** (e.g., Day 1 Morning)
2. **Open the exercise file** (e.g., `day1_morning_lists_tuples.py`)
3. **Fill in the `TODO` sections** with your implementation
4. **Run the unit tests** to verify your solutions:
   ```bash
   python -m pytest test_day1_morning_lists_tuples.py -v
   ```
5. **Iterate** until all tests pass
6. **Reference the guide** if you get stuck

### Running All Tests

To run all tests at once:
```bash
python -m pytest -v
```

To run tests for a specific day:
```bash
python -m pytest -k "day1" -v
python -m pytest -k "day2" -v
python -m pytest -k "day3" -v
python -m pytest -k "day4" -v
```

## The Comprehensive Guide

The file `python_coding_prep_days_1-4_comprehensive_guide.md` serves as your **solutions handbook and reference guide**. It contains:

- **Detailed explanations** of all concepts
- **Complete implementations** of all exercises
- **Theory and best practices** for each topic
- **Performance analysis** and complexity discussions
- **Additional examples** beyond the exercises

Use this guide to:
- Understand the concepts before attempting exercises
- Check your solutions against the reference implementations
- Learn about time and space complexity
- Explore alternative approaches and optimizations

## What Claude Code Did

Claude Code performed the following tasks to create this repository:

1. **Analyzed** the comprehensive guide to extract all key concepts and topics
2. **Designed** a structured codebase organized by days and sessions
3. **Generated** 8 exercise files with skeleton functions and TODO markers
4. **Created** 8 corresponding test files with comprehensive unit tests
5. **Ensured** that exercises progressively cover all topics from the guide
6. **Added** clear documentation and instructions for each exercise
7. **Structured** the repository for an optimal learning experience

## Files in This Repository

```
python4days/
├── README.md                                          # This file
├── python_coding_prep_days_1-4_comprehensive_guide.md # Reference guide
│
├── day1_morning_lists_tuples.py                       # Day 1 Morning exercises
├── test_day1_morning_lists_tuples.py                  # Day 1 Morning tests
│
├── day1_afternoon_dicts_sets.py                       # Day 1 Afternoon exercises
├── test_day1_afternoon_dicts_sets.py                  # Day 1 Afternoon tests
│
├── day2_morning_strings.py                            # Day 2 Morning exercises
├── test_day2_morning_strings.py                       # Day 2 Morning tests
│
├── day2_afternoon_complexity_sorting.py               # Day 2 Afternoon exercises
├── test_day2_afternoon_complexity_sorting.py          # Day 2 Afternoon tests
│
├── day3_morning_functions.py                          # Day 3 Morning exercises
├── test_day3_morning_functions.py                     # Day 3 Morning tests
│
├── day3_afternoon_recursion.py                        # Day 3 Afternoon exercises
├── test_day3_afternoon_recursion.py                   # Day 3 Afternoon tests
│
├── day4_morning_oop.py                                # Day 4 Morning exercises
├── test_day4_morning_oop.py                           # Day 4 Morning tests
│
├── day4_afternoon_patterns.py                         # Day 4 Afternoon exercises
└── test_day4_afternoon_patterns.py                    # Day 4 Afternoon tests
```

## Prerequisites

- **Python 3.8+** (tested with Python 3.8, 3.9, 3.10, 3.11)
- **pytest** for running tests:
  ```bash
  pip install pytest
  ```

## Learning Strategy

1. **Sequential Learning**: Follow the days in order, as concepts build upon each other
2. **Active Practice**: Don't just read solutions—implement them yourself
3. **Test-Driven**: Run tests frequently to get immediate feedback
4. **Deep Understanding**: Read the guide to understand WHY, not just HOW
5. **Iterate**: If a test fails, debug, learn, and try again

## Tips for Success

- **Read docstrings carefully** - they contain important hints
- **Start simple** - get basic functionality working, then optimize
- **Test frequently** - don't write all functions before testing
- **Use the guide** - it's there to help, not just for checking answers
- **Analyze complexity** - always consider time and space trade-offs
- **Explain your thinking** - verbalize your approach as if in an interview

## Additional Resources

- The comprehensive guide includes complexity analysis for all algorithms
- Each exercise is based on common coding interview patterns
- Solutions demonstrate best practices and Pythonic idioms

## License

This repository is for educational purposes. Feel free to use it for personal learning and interview preparation.

---

**Created by Claude Code** - An AI-powered coding assistant that transforms comprehensive guides into practical, hands-on learning experiences.
