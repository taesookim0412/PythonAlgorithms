import collections
from typing import List

#55.58
#13.44
#cbfrn
#TODO: Opposite of CBF
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        def dfs(board, node, i, j, path):
            if node.isWord:
                res.append(path)
                node.isWord = False
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = "#"
            dfs(board, node, i + 1, j, path + tmp)
            dfs(board, node, i - 1, j, path + tmp)
            dfs(board, node, i, j+1, path + tmp)
            dfs(board, node, i, j-1, path + tmp)
            board[i][j] = tmp



        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, node, i, j, "")
        return res



























#33/36 why no work?
class Solution2:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])
        letters = collections.defaultdict(list)
        foundWords = set()
        def dfs(word, i, j, idx, visited):
            if i < 0 or i >= len(board): return
            if j < 0 or j >= len(board[0]): return
            if board[i][j] != word[idx]: return
            for b in visited[i]:
                if b == j:
                    return
            visited[i] += j,
            if board[i][j] == word[idx]:
                print(idx, word, len(word), visited)
                idx += 1
            if idx == len(word):
                foundWords.add(word)
                return
            tmp = board[i][j]
            dfs(word, i, j + 1, idx, visited.copy())
            dfs(word, i, j - 1, idx, visited.copy())
            dfs(word, i - 1, j, idx, visited.copy())
            dfs(word, i + 1, j, idx, visited.copy())

        for i in range(len(words)):
            word = words[i]
            letters[word[0]] += i,
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                if letter in letters:
                    for idx in letters[letter]:
                        visited = collections.defaultdict(list)
                        dfs(words[idx], i, j, 0, visited.copy())
        print(np.asmatrix(board))
        if len(foundWords)== 0: return []
        return foundWords

import numpy as np
s = Solution()
# print(s.findWords([
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ],["oath","pea","eat","rain"]))

#Expected: []
print(s.findWords([["a","a"]],["aaa"]))
print(s.findWords([["a","b"],["c","d"]],
["acdb"]))

print(s.findWords([["a"]], ["a"]))
print(s.findWords([["a","b"],["c","d"]],
["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]))
print(s.findWords([["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]],
["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]))