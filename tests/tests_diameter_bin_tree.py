import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.diameter_of_binary_tree import max_diameter_of_binary_tree, BinaryTree

class TestBinaryTreeDiameter(unittest.TestCase):
    def test_example_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(3)
        tree.right = BinaryTree(2)
        tree.left.left = BinaryTree(7)
        tree.left.right = BinaryTree(4)
        tree.left.left.left = BinaryTree(8)
        tree.left.left.left.left = BinaryTree(9)
        tree.left.right.right = BinaryTree(5)
        tree.left.right.right.right = BinaryTree(6)

        self.assertEqual(max_diameter_of_binary_tree(tree), 6)

    # Add extra test given during the defence of the laboratory work
    def test_extra_example_tree(self):
        tree = BinaryTree(90)
        tree.left = BinaryTree(80)
        tree.right = BinaryTree(100)
        tree.left.left = BinaryTree(30)
        tree.left.right = BinaryTree(70)
        tree.left.left.left = BinaryTree(22)
        tree.left.left.left.left = BinaryTree(21)
        tree.left.right.left = BinaryTree(33)
        tree.left.right.left.right = BinaryTree(34)
        tree.left.right.left.left = BinaryTree(32)
        tree.left.right.left.left.left = BinaryTree(31)

        self.assertEqual(max_diameter_of_binary_tree(tree), 7)
        
    def test_empty_tree(self):
        self.assertEqual(max_diameter_of_binary_tree(None), 0)

    def test_one_node_tree(self):
        tree = BinaryTree(1)
        self.assertEqual(max_diameter_of_binary_tree(tree), 0)

    def test_one_level_tree(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(6)
        tree.right = BinaryTree(9)
        self.assertEqual(max_diameter_of_binary_tree(tree), 2)


if __name__ == "__main__":
    unittest.main()
