import collections
import numpy as np
from typing import List
import re
import math

#Runtime: 52 ms, faster than 58.45% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 15.3 MB, less than 21.76% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        expressed_Word = re.sub('[^A-Za-z0-9]', '', s).lower()
        L = expressed_Word[:len(expressed_Word)//2]
        R = expressed_Word[math.ceil(len(expressed_Word)/2):][::-1]
        return L == R

s = Solution()
#Amanaplana
#c
#Amanaplana
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome('ab_a'))