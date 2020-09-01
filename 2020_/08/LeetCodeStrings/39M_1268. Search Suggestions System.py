import collections
import numpy as np
from typing import List

#could binary search the products instead of a linear scan.

# Runtime: 148 ms, faster than 68.26% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 16.5 MB, less than 59.63% of Python3 online submissions for Search Suggestions System.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = [[] for _ in range(len(searchWord))]
        products.sort()
        word = ""
        for i, c in enumerate(searchWord):
            word += c
            for prod in products:
                if prod.startswith(word):
                    res[i].append(prod)
                if len(res[i]) == 3:
                    break
            if len(res[i]) == 0:
                break
        return res

# Runtime: 548 ms, faster than 25.00% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 16.4 MB, less than 81.93% of Python3 online submissions for Search Suggestions System.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = [[] for _ in range(len(searchWord))]
        products.sort()
        word = ""
        for i, c in enumerate(searchWord):
            word += c
            for prod in products:
                if prod.startswith(word):
                    res[i].append(prod)
                if len(res[i]) == 3:
                    break
        return res

# Runtime: 648 ms, faster than 18.46% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 22.1 MB, less than 6.55% of Python3 online submissions for Search Suggestions System.
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

    #V char in word:
    #dfs @ char level (PATH = :char)
    #Runtime: 648 ms, faster than 18.46% of Python3 online submissions for Search Suggestions System.
    #Memory Usage: 22.1 MB, less than 6.55% of Python3 online submissions for Search Suggestions System.
    def search(self, word):
        curr = self.root
        word_substr = ""
        self.res = [[] for _ in range(len(word))]
        for i, c in enumerate(word):
            word_substr += c
            if curr.children[c]:
                curr = curr.children[c]
                self.dfs(curr, word_substr, i)
        return self.res

    def dfs(self, tn, path, i):
        if len(self.res[i]) == 3:
            return
        if len(self.res[i]) != 3 and tn.isWord:
            self.res[i].append(path)
        for k, v in tn.children.items():
            self.dfs(tn.children[k], path + k, i)

    # Runtime: 1108 ms, faster than 6.97% of Python3 online submissions for Search Suggestions System.
    # Memory Usage: 21.9 MB, less than 7.02% of Python3 online submissions for Search Suggestions System.
    # def search(self, word):
    #     self.res = []
    #     curr = self.root
    #     for c in word:
    #         if curr.children[c]:
    #             curr = curr.children[c]
    #         else:
    #             return []
    #     # curr points to the current TrieNode
    #     self.dfs(curr, word)
    #     return self.res
    #
    # def dfs(self, tn, path):
    #     if len(self.res) == 3:
    #         return
    #     if len(self.res) != 3 and tn.isWord:
    #         self.res.append(path)
    #     for k, v in tn.children.items():
    #         self.dfs(tn.children[k], path + k)


class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tn = Trie()
        for prod in sorted(products):
            tn.insert(prod)
        return tn.search(searchWord)

s = Solution()
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))