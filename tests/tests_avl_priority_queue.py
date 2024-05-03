import unittest
import sys
import os

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.avl_priority_queue import AVLTree_Priority_Queue


class TestAVLTreePriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = AVLTree_Priority_Queue()

    def test_insert_and_peek(self):
        self.queue.insert(10, 2)
        self.queue.insert(20, 1)
        self.assertEqual(self.queue.peek(), 10)

    def test_remove_highest_priority_node(self):
        self.queue.insert(10, 2)
        self.queue.insert(20, 1)
        self.assertEqual(self.queue.remove_highest_priority_node(), 20)

    def test_view_priority_queue(self):
        self.queue.insert(10, 2)
        self.queue.insert(20, 1)
        queue_content = self.queue.view_priority_queue()
        sorted_queue_content = sorted(queue_content, key=lambda x: x[1])
        self.assertEqual(sorted_queue_content, [(20, 1), (10, 2)])

    def test_peek_empty_queue(self):
        self.assertIsNone(self.queue.peek())

    def test_remove_from_empty_queue(self):
        self.assertIsNone(self.queue.remove_highest_priority_node())

    def test_delete_node_from_empty_queue(self):
        self.assertIsNone(self.queue._delete_node(self.queue.root, 5))


if __name__ == "__main__":
    unittest.main()
