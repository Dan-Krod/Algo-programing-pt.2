import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.min_path_chess_hourse import get_min_distance_of_chess_horse


class TestChessPath(unittest.TestCase):

    def test_files_with_value(self):
        file_input = "resources/test_input.txt"
        file_output = "resources/test_output.txt"
        get_min_distance_of_chess_horse(file_input, file_output)
        with open(file_output, "r") as file:
            result = int(file.read())
        file.close()
        self.assertEqual(result, 6)

    def test_empty_files(self):
        empty_file_input = "resources/test_empty_input.txt"
        empty_file_output = "resources/test_empty_output.txt"
        get_min_distance_of_chess_horse(empty_file_input, empty_file_output)
        with open(empty_file_output, "r") as file:
            result = int(file.read())
        file.close()
        self.assertEqual(result, -1)

    def test_wrong_files(self):
        wrong_file_input = "resources/test_wrong_input.txt"
        wrong_file_output = "resources/test_wrong_output.txt"
        get_min_distance_of_chess_horse(wrong_file_input, wrong_file_output)
        with open(wrong_file_output, "r") as file:
            result = int(file.read())
        file.close()
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
