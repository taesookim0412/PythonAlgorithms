import collections
import numpy as np
from typing import List

#Runtime: 52 ms, faster than 84.59% of Python3 online submissions for Reverse Vowels of a String.
#Memory Usage: 15 MB, less than 36.79% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u', 'A','E','I','O','U'}
        s = list(s)
        removals = []
        for i, c in enumerate(s):
            if c in vowels:
                removals += c,
                s[i] = ''
        for i, c in enumerate(s):
            if c == '':
                s[i] = removals.pop()
        return ''.join(s)
