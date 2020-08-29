import collections
import numpy as np
from typing import List

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products = sorted(products)
#         res = [[] for _ in range(len(searchWord))]
#         curWord = ""
#         for i, c in enumerate(searchWord):
#             curWord += c
#             for j in range(len(products)-1, -1, -1):
#                 print(products)
#                 p = products[j]
#                 if p >= curWord and len(p) > i and p[i] <= curWord[i]:
#                     res[i] += p,
#                 if len(res[i]) == 3 or j == 0:
#                     break
#         return res

# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.isWord = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def insert(self, word):
#         node = self.root
#         for c in word:
#             node = node.children[c]
#         node.isWord = True
#     def search(self, word):
#         node = self.root
#         for c in word:
#             node = node.children.get(c)
#             if not node:
#                 return False
#         return node.isWord








s = Solution()
#[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))

#[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
print(s.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))
