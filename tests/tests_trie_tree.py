import unittest
from src.trie_tree import Trie, trie_tree_fill


class TestTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert_word("apple")
        trie.insert_word("banana")
        self.assertEqual(trie.search_word("apple"), True)
        self.assertEqual(trie.search_word("ape"), False)

    def test_search_prefix(self):
        trie = Trie()
        trie.insert_word("apple")
        trie.insert_word("melon")
        trie.insert_word("pinapple")
        found, words_with_prefix = trie.search_prefix("app")
        self.assertTrue(found)
        self.assertIn("apple", words_with_prefix)
        found, words_with_prefix = trie.search_prefix("pinn")
        self.assertFalse(found)
        self.assertEqual(words_with_prefix, [])

    def test_empty_search(self):
        trie = Trie()
        self.assertEqual(trie.search_word("apple"), False)
        self.assertEqual(trie.search_prefix("app"), False)

    def test_trie_tree_fill_function(self):
        trie = trie_tree_fill(["apple", "blitz", "applepen", "pinapplepen"])
        self.assertTrue(trie.search_word("apple"))
        self.assertFalse(trie.search_word("app"))
        self.assertTrue(trie.search_prefix("app")[0])
        self.assertFalse(trie.search_prefix("pinn")[0])

    def test_delete(self):
        trie = trie_tree_fill(["apple", "banana", "orange"])
        self.assertEqual(trie.delete("banana"), "banana")


if __name__ == "__main__":
    unittest.main()
