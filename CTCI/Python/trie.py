import typing


# Not optimized simple implementation of a trie using hash tables
class HashTrieNode(object):
    def __init__(self):
        self.children: dict = {}
        self.last: bool = False


# And using a fixed-length array based on 26-character alphabet
class LowercaseTrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.last: bool = False


class Trie(object):  # currently implemented using HashTrieNode
    def __init__(self):
        self.root = HashTrieNode()
        self._word_list = []

    def add_words(self, word_list: typing.List[str]):
        for word in word_list:
            self.insert(word)

    def insert(self, word: str):
        cursor = self.root
        for char in list(word):
            if char not in cursor.children:
                cursor.children[char] = HashTrieNode()
            cursor = cursor.children[char]
        cursor.last = True

    def __contains__(self, item):
        return self.contains(item)

    def contains(self, word: str) -> bool:
        cursor = self.root
        found = True
        for char in list(word):
            if char not in cursor.children:
                return False
            cursor = cursor.children[char]
        return cursor and cursor.last and found

    def _prefix_rec(self, node: HashTrieNode, word: str):
        if node.last:
            self._word_list.append(word)
        for char, n in node.children.items():
            self._prefix_rec(n, word + char)

    def all_words_with_prefix(self, key: str) -> typing.List[str]:
        self._word_list = []
        node = self.root
        temp_word = ''

        for char in list(key):
            if char not in node.children:
                return []
            temp_word += char
            node = node.children[char]

        self._prefix_rec(node, temp_word)
        return self._word_list


if __name__ == '__main__':
    keys = ['hello', 'dog', 'hell', 'cat', 'hel', 'help', 'helping']
    search_key = 'hel'
    t = Trie()
    t.add_words(keys)
    print(keys)
    print('Search Word:', search_key)
    print('Words Found:', t.all_words_with_prefix(search_key))
    print('"hel" in Trie:', 'hel' in t)
