import numpy as np

#05-14-2020_
#https://leetcode.com/problems/longest-common-subsequence/submissions/
#Runtime: 452 ms, faster than 69.29% of Python3 online submissions for Longest Common Subsequence.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Longest Common Subsequence.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if (len(text2) > len(text1)): return self.longestCommonSubsequence(text2, text1)
        mtx = [[0] * (len(text2)+1) for _ in range(2)]
        for i, a in enumerate(text1):
            for j, b in enumerate(text2):
                if (a==b): mtx[1 - i%2][j+1] = 1 + mtx[i%2][j]
                else: mtx[1 - i%2][j+1] = max(mtx[i%2][j+1], mtx[1- i%2][j])
        return mtx[-1][-1]
        
        
    def __init__(self):
        print(self.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
        print(self.longestCommonSubsequence("abcde", "ace"))
        

Solution()