import collections
import numpy as np
from typing import List
import math

#Runtime: 120 ms, faster than 75.52% of Python3 online submissions for Valid Palindrome II.
#Memory Usage: 14.1 MB, less than 84.55% of Python3 online submissions for Valid Palindrome II.

#My Post:
#https://leetcode.com/problems/valid-palindrome-ii/discuss/806397/Python-Lots-of-confusion-LR-Partition-String-Slice

#Maxmimum one deletion
#So L == R in our previous case
#With one deletion (L == R) with 1 off!
class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = s[:math.ceil(len(s)/2)]
        R = s[math.ceil(len(s) / 2):][::-1]
        if L == R: return True
        print (L, R)
        i = 0
        while i < len(L) and i < len(R) and L[i] == R[i]:
            i+=1
        # print(L[i:] + R[i+1:], (L[i:] + R[i+1:][::-1])[::-1],
        #       L[i + 1:] + R[i:], (L[i + 1:] + R[i:][::-1])[::-1]
        #       )
        str1 = L[i:] + R[i+1:][::-1]
        str2 = L[i+1:] + R[i:][::-1]
        return str1 == str1[::-1] or str2 == str2[::-1]


s = Solution()
#remove a
print(s.validPalindrome("ssa"))
#remove C
print(s.validPalindrome("abac"))
#True
print(s.validPalindrome("abab"))
#True
print(s.validPalindrome("abba"))
#True
print(s.validPalindrome("ababa"))
print(s.validPalindrome("deeee"))
print(s.validPalindrome("tcaac"))


print('\n\n\n')

#LS: 2 C's, RS: 1A, 1B
#Problem: +2 on LS, -2 on RS
print(s.validPalindrome("cacaba"))
print(s.validPalindrome("cacabcaca"))
