# COMP100 2025F Lab 11: Error Checking / Exception Handling
# Q1: Robust Arithmetic Operations

We've provided a basic implementation of the function `print_operation` in the file "q1.py". This function performs arithmetic operations on two numbers, given as string inputs, along with a specified arithmetic operator (`'+', '-', '*', '/'`).

**Objective:**  
Refine the function `print_operation` by incorporating assertions and raising appropriate exceptions to handle various error scenarios. Your implementation should address the following cases:

- The arithmetic operation provided is not one of the allowed operations (`+`, `-`, `*`, `/`). For this, raise a `ValueError` with error message: `"Unsupported operation. Use '+', '-', '*', or '/'."`.
- The input strings cannot be converted into integers. For this, raise a `ValueError` with error message: `"Input strings must be convertible to integers."`.
- A division by zero occurs during a division operation. For this, raise a `ZeroDivisionError` with error message: `"Division by zero is not allowed."`.

Each exception should provide a clear error message detailing what went wrong. If the function completes without errors, it should return the result as a string, unless an optional argument specifies to print the result.

**Example Usage:**

```python
print_operation("5", "2", "+")  # should return "5 + 2 = 7"
print_operation("5", "0", "/")  # should raise ZeroDivisionError with message "Division by zero is not allowed."
```

# Q2: File Content Validator

In this task, you will implement a function `validate_file_contents` in "q2.py" that reads and validates the content of a file based on specific criteria. This function should use a custom exception to handle various validation failures.

**Custom Exception:**
- **`FileValidationError`**: This exception provides detailed information about the validation failure. It accepts multiple parameters to help deliver a comprehensive error message.

**Function Specifications:**
- **Parameters**: The function takes a file path, the expected number of lines in the file, and a keyword that must appear at least once in the file.
- **Behavior**: The function opens and reads the file, checks if the number of lines matches the expected count, and ensures the keyword is present at least once. If the file does not meet these criteria, the function raises `FileValidationError` with details about the specific failure(s).
- **Normal Output**: If the file meets all validation criteria, the function returns "File validation passed."
- **Error Handling**: If the file cannot be found, the function returns "File not found."

**Details of Custom Exception Handling**:
- **Missing Lines**: This parameter indicates the discrepancy between the expected and actual number of lines. It is calculated as `expected_lines - actual_lines`. A positive number indicates fewer lines than expected, and a negative number indicates more lines than expected.
- **Missing Keyword**: This indicates that a required keyword is not found in the file.

For more detailed guidance on implementing these functionalities, refer to the template provided in "q2.py". This template outlines where to add code for reading the file, checking line counts, searching for the keyword, and constructing detailed error messages.

# Q3: Date Parser with Validation

Implement a function called `parse_date(year_str, month_str, day_str)` that:

1. Attempts to convert `year_str`, `month_str`, and `day_str` into integers.
2. Validates that the year is between 1900 and 2100.
3. Validates that the month is between 1 and 12.
4. Validates that the day is valid for the given month and year (e.g., February 30 should not be allowed).
5. Returns the date as a string

Use Python's `datetime` module to attempt creating a `datetime.date` object. This will naturally raise a `ValueError` for invalid dates, which you should catch and re-raise with a more descriptive message.

**Example Usage of `datetime.date` function:**
```python
  year = 2024
  month = 12
  day = 30

  date = datetime.date(year, month, day)
  print(date) # Output: 2020-02-29
```

**Error Conditions:**

- If any of `year_str`, `month_str`, or `day_str` cannot be converted to an integer, raise a `ValueError` with the message:  
  `"Year, month, and day strings must contain integers."`

- If `year` is outside the range [1900, 2100], raise a custom exception `YearRangeError` with the message:  
  `"Year must be between 1900 and 2100."`

- If the date is invalid (e.g., April 31, or month=13, or day=0), raise a `ValueError` with the message:  
  `"Invalid date specified."`

**If Successful:**  
Return the date as a string in the format `"YYYY-MM-DD"`.

**Example Usage:**
```python
parse_date("2020", "02", "29")  # returns "2020-02-29"
parse_date("1899", "12", "15")  # raises YearRangeError("Year must be between 1900 and 2100.")
parse_date("2021", "13", "10")  # raises ValueError("Invalid date specified.")
parse_date("2021", "Feb", "10") # raises ValueError("Year, month, and day must be integers.")
```

### Q4: Tab-Delimited File Validator

Implement a function `validate_tab_file(file_path, expected_fields, required_pattern)` that:

1. Attempts to open and read a file line-by-line.
2. Checks that each line contains exactly `expected_fields` fields, separated by tabs (`'\t'`).
3. Confirms that **at least one line** contains a field that matches the given `required_pattern` (a substring).

You will create and use a custom exception `TabFileValidationError` to handle validation failures.

**Behavior:**

- If the file is not found, return `"File not found."`

- If any line does not have the correct number of fields (`expected_fields`), raise `TabFileValidationError`.  
  Include in the exception message:
  - The `file_path`
  - The line number (1-based index) of the first offending line
  - The discrepancy in the number of fields found vs. expected

- If none of the lines contains a field that includes `required_pattern` as a substring, raise `TabFileValidationError` indicating the missing pattern.

**Normal Output:**  
If all criteria are met, return `"Tab-delimited file validation passed."`

**Custom Exception Details:**

- `TabFileValidationError` should provide clear, detailed information. For example:
  - If a line is malformed:  
    `"File path: data.txt, Line 3: Expected 4 fields, found 2."`
  - If the required pattern is missing:  
    `"File path: data.txt, No field contains required pattern 'user_id'."`

- `FileNotFoundError` should provide:
  - `File Not Found.` If the file does not exist.


**Example Usage:**
```python
# Suppose data.txt contents are:
# name    age    country    email
# John    30     Canada     john@example.com
# Alice   25     USA        alice@example.com

validate_tab_file("data.txt", expected_fields=4, required_pattern="example")  
# returns "Tab-delimited file validation passed."

validate_tab_file("data.txt", expected_fields=4, required_pattern="missing_pattern")  
# raises TabFileValidationError("File path: data.txt, No field contains required pattern 'missing_pattern'.")

validate_tab_file("missing_file.txt", 4, "example")  
# returns "File not found."

# If data.txt had a line with fewer fields, for example:
# John    30    Canada

validate_tab_file("data.txt", 4, "example")
# raises TabFileValidationError("File path: data.txt, Line 2: Expected 4 fields, found 3.")
```
 
