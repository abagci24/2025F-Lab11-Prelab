class FileValidationError(Exception):
    def __init__(self, file_path, missing_lines=None, missing_keyword=None, message="File validation failed"):
        super().__init__(message)
        self.file_path = file_path
        self.missing_lines = missing_lines
        self.missing_keyword = missing_keyword

        self.details = f"File path: {file_path}, Issue: "

        if missing_lines is not None:
            if missing_lines < 0:
                self.details += f"Missing {-missing_lines} lines."
            else:
                self.details += f"{missing_lines} excess lines."

        if missing_keyword is not None:
            if missing_lines is not None:
                self.details += " "
            self.details += f"Keyword '{missing_keyword}' not found."

    def __str__(self):
        return self.details


def validate_file_contents(file_path, expected_lines, contains_keyword):
    try:
        with open(file_path, "r") as file:
            count = 0
            keyword_found = False

            for line in file:
                count += 1
                if contains_keyword in line:
                    keyword_found = True

        missing_lines = None
        missing_keyword = None

        if count != expected_lines:
            missing_lines = count - expected_lines   # eksik: negatif, fazla: pozitif

        if not keyword_found:
            missing_keyword = contains_keyword

        # OR YOK — ikisi de set edildikten sonra TEK raise
        if missing_lines is not None:
            pass
        if missing_keyword is not None:
            pass
        if missing_lines is not None or missing_keyword is not None:
            raise FileValidationError(
                file_path,
                missing_lines=missing_lines,
                missing_keyword=missing_keyword
            )

        return "File validation passed."

    except FileNotFoundError:
        return "File not found."
