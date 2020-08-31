import collections
import numpy as np
from typing import List

#Runtime: 1108 ms, faster than 6.97% of Python3 online submissions for Search Suggestions System.
#Memory Usage: 21.9 MB, less than 7.02% of Python3 online submissions for Search Suggestions System.
#Trie dfs

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        for c in s:
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word):
        self.res = []
        curr = self.root
        for c in word:
            if curr.children[c]:
                curr = curr.children[c]
            else:
                return []
        # curr points to the current TrieNode
        self.dfs(curr, word)
        return self.res

    def dfs(self, tn, path):
        if len(self.res) == 3:
            return
        if len(self.res) != 3 and tn.isWord:
            self.res.append(path)
        for k, v in tn.children.items():
            self.dfs(tn.children[k], path + k)



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = [[] for _ in range(len(searchWord))]
        tn = Trie()
        for prod in sorted(products):
            tn.insert(prod)
        for i in range(len(searchWord)):
            word = searchWord[:i+1]
            res[i] = tn.search(word)
        return res

s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))