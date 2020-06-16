#
#Runtime: 240 ms, faster than 30.66% of Python3 online submissions for Implement Trie (Prefix Tree).
#Memory Usage: 33.1 MB, less than 10.08% of Python3 online submissions for Implement Trie (Prefix Tree).

class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for i, a in enumerate(word):
            charI = ord(a) - ord('a')
            if not root.children[charI]:
                root.children[charI] = TrieNode()
            root = root.children[charI]
        root.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for i, a in enumerate(word):
            charInt = ord(a) - ord('a')
            if not root.children[charInt]:
                return False
            root = root.children[charInt]
        return root.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for i, a in enumerate(prefix):
            charInt = ord(a) - ord('a')
            if not root.children[charInt]:
                return False
            root = root.children[charInt]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "word"
obj.insert(word)

param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith("wor")
print(param_3)