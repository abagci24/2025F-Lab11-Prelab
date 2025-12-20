import os
import unittest
from q2 import FileValidationError, validate_file_contents

class TestFileValidation(unittest.TestCase):

    def setUp(self):
        # Creating a sample file for testing
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, 'w') as f:
            f.write("Python\nTutorial\nExample\nText\n")

    def tearDown(self):
        # Remove the test file after testing
        os.remove(self.test_file_path)

    def test_file_validation_pass(self):
        # Test where file validation should pass
        result = validate_file_contents(self.test_file_path, 4, 'Python')
        self.assertEqual(result, "File validation passed.")

    def test_file_not_found(self):
        # Test file not found error handling
        result = validate_file_contents("nonexistent.txt", 5, 'data')
        self.assertEqual(result, "File not found.")

    def test_incorrect_line_count(self):
        # Test handling of incorrect number of lines
        with self.assertRaises(FileValidationError) as context:
            validate_file_contents(self.test_file_path, 5, 'Python')
        self.assertIn("Missing 1 lines", str(context.exception))

    def test_missing_keyword(self):
        # Test handling when keyword is missing
        with self.assertRaises(FileValidationError) as context:
            validate_file_contents(self.test_file_path, 4, 'Java')
        self.assertIn("Keyword 'Java' not found", str(context.exception))


if __name__ == '__main__':
    unittest.main()
