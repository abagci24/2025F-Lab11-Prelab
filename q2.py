class FileValidationError(Exception):
    def __init__(self, file_path, missing_lines=None, missing_keyword=None, message="File validation failed"):
        super().__init__(message)
        self.file_path = file_path  # Store the path of the file that triggered the exception
        self.missing_lines = missing_lines  # The difference in the expected and actual line count
        self.missing_keyword = missing_keyword  # The keyword that was expected but not found

        # TODO: Enhance the initial error message by appending specific details about the validation failure.
        # Start by declaring a base message structure mentioning the file path and a general issue statement.
        self.details = f"File path: {file_path}, Issue: "

        # If missing_lines is provided (not None), it indicates the expected and actual line counts differ.
        # Append a message detailing the number of lines that are missing or in excess.
        # Example: If missing_lines is -3, append "Missing 3 lines." to self.details.
        # If missing_lines is 3, append "3 excess lines." to self.details.

        # If missing_keyword is provided (not None), it indicates a specific keyword was expected in the file but wasn't found.
        # Append a message stating the keyword and noting its absence.
        # Example: If missing_keyword is "function", append "Keyword 'function' not found." to self.details.

        # Each condition should enhance the details attribute, making the error message more informative and specific
        # to the encountered issue, thus aiding in quicker debugging and resolution.

    def __str__(self):
        return f"{self.details}"


def validate_file_contents(file_path, expected_lines, contains_keyword):
    try:
        with open(file_path, 'r') as file:
            pass
            # TODO: Read lines from the file and determine the actual number of lines.
            # If the actual number of lines does not match expected_lines, raise FileValidationError.
            # You need to calculate the difference between actual and expected lines and pass it to the exception.

            # TODO: Check if the file contents contain a specific keyword.
            # If the keyword is not found, raise FileValidationError with the missing keyword.
        return "File validation passed."

    except FileNotFoundError:
        return "File not found."
