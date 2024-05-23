import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.longest_word_chain import longest_word_chain

class TestLongestWordChain(unittest.TestCase):
    def test_word_chain_example_1(self):
        input_file = "resources/wchain_1.in"
        output_file = "resources/wchain_1.out"
        longest_word_chain(input_file, output_file)
        with open(output_file, "r") as file:
            result = int(file.read())
        file.close()
        self.assertEqual(result, 6)
        
    def test_word_chain_example_2(self):
        input_file = "resources/wchain_2.in"
        output_file = "resources/wchain_2.out"
        longest_word_chain(input_file, output_file)
        with open(output_file, "r") as file:
            result = int(file.read())
        file.close()
        self.assertEqual(result, 4)
        
    def test_word_chain_example_3(self):
        input_file = "resources/wchain_3.in"
        output_file = "resources/wchain_3.out"
        longest_word_chain(input_file, output_file)
        with open(output_file, "r") as file:
            result = int(file.read())
        file.close()
        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()