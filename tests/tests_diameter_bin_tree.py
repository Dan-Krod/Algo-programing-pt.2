import unittest
from diameter_binary_tree import max_diameter_of_binary_tree, BinaryTree

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
