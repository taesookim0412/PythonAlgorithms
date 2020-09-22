import collections
import numpy as np
from typing import List


#Runtime: 300 ms, faster than 22.56% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
#Memory Usage: 14.6 MB, less than 69.19% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        numVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowelCt = sum(x in vowels for x in s[:k])
        for j in range(len(s) - k + 1):
            #window = s[j:j+k]
            #print(window)
            if j != 0:
                prev = s[j-1]
                curr = s[j+k-1]
                vowelCt += curr in vowels
                vowelCt -= prev in vowels
            numVowels = max(vowelCt, numVowels)
            if numVowels == k:
                break
        return numVowels
    def maxVowels3(self, s: str, k: int) -> int:
        numVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowelCt = sum(x in vowels for x in s[:k])
        for j in range(len(s) - k + 1):
            #window = s[j:j+k]
            #print(window)
            if j != 0:
                prev = s[j-1]
                curr = s[j+k-1]
                vowelCt += curr in vowels
                vowelCt -= prev in vowels
            numVowels = max(vowelCt, numVowels)
            if numVowels == k:
                break
        return numVowels

    # Runtime: 720 ms, faster than 5.05% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    # Memory Usage: 14.7 MB, less than 44.78% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    def maxVowels2(self, s: str, k: int) -> int:
        numVowels = 0
        vowels = ['a','e','i','o','u']
        ctr = collections.Counter(s[:k])
        for j in range(len(s) - k + 1):
            #window = s[j:j+k]
            #print(window)
            if j != 0:
                prev = s[j-1]
                ctr[s[j+k-1]] += 1
                if ctr[prev] == 1:
                    del ctr[prev]
                else:
                    ctr[prev] -= 1
            numVowels = max(sum([ctr[vowel] for vowel in vowels]), numVowels)
            if numVowels == k:
                break
        return numVowels


s = Solution()
print(s.maxVowels("abciiidef", 3))
print(s.maxVowels("hyuna", 3))
print(s.maxVowels("abcd", 3))



