import collections
from typing import List



#27 / 36 test cases passed.
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])
        letters = collections.defaultdict(dict)
        foundWords = set()
        def dfs(word, i, j, idx, visited):
            if idx == len(word):
                foundWords.add(word)
                return
            if i < 0 or i >= len(board): return
            if j < 0 or j >= len(board[0]): return
            if board[i][j] != word[idx]: return
            for b in visited[i]:
                if b == j:
                    return
            visited[i] += j,
            if board[i][j] == word[idx]:
                idx += 1
            dfs(word, i, j + 1, idx, visited.copy())
            dfs(word, i, j - 1, idx, visited.copy())
            dfs(word, i - 1, j, idx, visited.copy())
            dfs(word, i + 1, j, idx, visited.copy())

        for i in range(len(words)):
            word = words[i]
            letters[word[0]] = i
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                if letter in letters:
                    idx = letters[letter]
                    visited = collections.defaultdict(list)
                    dfs(words[idx], i, j, 0, visited)
        if len(foundWords)== 0: return []
        return foundWords


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
