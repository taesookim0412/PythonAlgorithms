# -*- coding: utf-8 -*-

#https://leetcode.com/problems/longest-common-subsequence/submissions/
#Runtime: 416 ms, faster than 84.12% of Python3 online submissions for Longest Common Subsequence.
#Memory Usage: 21.6 MB, less than 100.00% of Python3 online submissions for Longest Common Subsequence.
#TODO: Reduce memory to be N*2

import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #x: Text2
        #y: Text1
        mtx = [[0] * (len(text2) +1) for _ in range(len(text1) +1)]
        for i, b in enumerate(text1):
            for j, a in enumerate(text2):
                if (a==b): 
                    mtx[i+1][j+1] += 1 + mtx[i][j]
                else: mtx[i+1][j+1] = max(mtx[i][j+1], mtx[i+1][j])
        print(np.matrix(mtx))
        #print(mtx[-1][-1])
        return(mtx[-1][-1])
    
    def __init__(self):
        #print(self.longestCommonSubsequence("XMJYAUZ", "MZJAWXU"))
        print(self.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
        print(self.longestCommonSubsequence("abcde", "ace"))
            
            
        
Solution()
#print(Solution().longestCommonSubsequence("abcde", "abce"))
#print(Solution().longestCommonSubsequence("asdfghj", "jsdh"))
#print(Solution().longestCommonSubsequence("def", "abc"))