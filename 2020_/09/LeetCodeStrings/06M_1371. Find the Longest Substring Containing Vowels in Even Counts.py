import collections
import numpy as np
from typing import List


# good sliding window practice
# Runtime: 680 ms, faster than 46.10% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.
# Memory Usage: 19.5 MB, less than 30.73% of Python3 online submissions for Find the Longest Substring Containing Vowels in Even Counts.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def countVowels(ct):
            if not ct['a'] % 2 and not ct['e'] % 2 and not ct['i'] % 2 and not ct['o'] % 2 and not ct['u'] % 2:
                return True
            return False

        #Reducer
            #Slider
            #0 - len(s)
            #0 - len(s) -1 -> 1 - len(s)
        for i in range(len(s)):
            ctr = collections.Counter(s[:len(s) - i])
            for j in range(i+1):
                #window = s[j:(len(s)+j) - i]
                if j != 0:
                    ctr[s[j - 1]] -= 1
                    ctr[s[len(s)+j - i - 1]] += 1
                if countVowels(ctr):
                    return sum(ctr.values())
        return 0


# s = "leetcodeisgreat"
# Explanation: The longest substring is "leetc" which contains two e's.
# 5
#"id" returns 1
class Solution2:
    def findTheLongestSubstring(self, s: str) -> int:
        def countVowels(s):
            ct = collections.Counter(s)
            if not ct['a'] % 2 and not ct['e'] % 2 and not ct['i'] % 2 and not ct['o'] % 2 and not ct['u'] % 2:
                return True
            return False
        biggestLen = 0
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                newStr = s[i:j+1]
                if countVowels(newStr):
                    biggestLen = max(biggestLen, len(newStr))
        return biggestLen


s = Solution()
print(s.findTheLongestSubstring("eleetminicoworoep"))
print(s.findTheLongestSubstring("leetcodeisgreat"))
print(s.findTheLongestSubstring("bcbcbc"))
# print(s.findTheLongestSubstring("abcd"))

