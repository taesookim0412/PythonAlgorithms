import collections
import numpy as np
from typing import List


#Runtime: 172 ms, faster than 5.11% of Python3 online submissions for Palindrome Partitioning.
#Memory Usage: 14 MB, less than 78.81% of Python3 online submissions for Palindrome Partitioning.
#i am a monster
class Solution:
    def partitionString(self, s):
        res = []
        def backtrack(path, j, idx):
            if idx == len(s):
                res.append(path)
            for i in range(j, len(s)):
                if s[j:i+1] == s[j:i+1][::-1]:
                    newlen = idx + i+1-j
                    backtrack(path + [s[j:i+1]], i+1, newlen)
        backtrack([], 0, 0)
        return res

#Here's an attempt at an alternative algorithm (although readability is pretty trivial here,
#it can't quite be resolved without some serious debugging.
#Okay
#This returns the same initial string.
class Solutionlele:
    def partitionString(self, s):
        res = []
        def backtrack(path, j, idx):
            if idx == len(s):
                res.append(path)
            for i in range(j, len(s)+1):
                backtrack(path + [s[j-1:i]], i+1, idx + 1)
        backtrack([], 1, 0)
        return res


class Solution2:
    def partitionString(self, s):
        res = []
        def backtrack(path,partition, depth):
            if not partition:
                res.append(path)
            for i in range(1, len(partition)+1):
                #newString = partition[i:]
                #print(f"{path} {partition[:i]:2}")
                #print(f"depth: {depth}", " |       ", newString, " | From: |", partition, i)
                #[:i], [i]: Non inclusive [:i], Inclusive [i:] Therefore the entire string is always preserved
                #And the base case will always hold (there is no string remaining).
                backtrack(path + [partition[:i]], partition[i:],depth+1)
        backtrack([], s, 0)
        return res

s = Solution()
print(s.partitionString("aab"))
s2 = Solution2()
print(s2.partitionString("aab"))
