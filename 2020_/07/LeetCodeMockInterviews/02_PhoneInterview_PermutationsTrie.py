import collections
import numpy as np
from typing import List

# Random Set- Phone Interview
# CompletedJuly 14, 2020_ 9:50 AM
# Time Spent: 29 minutes 56 seconds
# Time Allotted: 1 hour 30 minutes
#15/15

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isTail = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.children = self.root.children

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            letter = ord(c) - 97
            if not curr.children[letter]:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.isTail = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            letter = ord(c) - 97
            if not curr.children[letter]:
                return False
            curr = curr.children[letter]
        return curr.isTail

    def startsWith(self, prefix: str) -> bool:
        r"""
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            letter = ord(c) - 97
            if not curr.children[letter]:
                return False
            curr = curr.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#25/25
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(size):
            if size==1:
                res.append(nums.copy())
            for i in range(size):
                backtrack(size-1)
                if size &1:
                    nums[i], nums[size-1] = nums[size-1], nums[i]
                else:
                    nums[0], nums[size-1] = nums[size-1], nums[0]
        backtrack(len(nums))
        return res