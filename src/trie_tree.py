class TrieNode:
    def __init__(self, end_part_of_word: bool = False, data: str = ""):
        self.children = {}
        self.end_part_of_word = end_part_of_word
        self.data = data


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        cur_el = self.root
        for ch, letter in enumerate(word):
            if letter not in cur_el.children:
                prefix = word[: ch + 1]
                cur_el.children[letter] = TrieNode(data=prefix)
                cur_el = cur_el.children[letter]
            else:
                cur_el = cur_el.children.get(letter)
        if cur_el.end_part_of_word:
            return False
        cur_el.end_part_of_word = True
        return True

    def search_word(self, word):
        if self.root.children == {}:
            return False

        cur_el = self.root
        for ch in word:
            if ch not in cur_el.children:
                return False
            cur_el = cur_el.children[ch]
        return cur_el.end_part_of_word

    def _find_child_words(self, current, words):
        if current.end_part_of_word:
            words.append(current.data)

        for letter in current.children:
            self._find_child_words(current.children[letter], words)

    def search_prefix(self, prefix):
        if self.root.children == {}:
            return False
        cur_el = self.root
        words = []
        found = False
        for ch in prefix:
            if ch not in cur_el.children:
                return found, words
            cur_el = cur_el.children[ch]
        self._find_child_words(cur_el, words)
        found = bool(words)
        return found, words

    def delete(self, word):
        node_to_delete = self.search_word(word)
        if node_to_delete:
            # node_to_delete.end_part_of_word = False
            return word
        return None


def trie_tree_fill(words):
    trie = Trie()
    for word in words:
        trie.insert_word(word)
    return trie
