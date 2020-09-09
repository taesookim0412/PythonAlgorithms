import collections
import numpy as np
from typing import List


# good sliding window practice


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def countVowels(s):
            ct = collections.Counter(s)
            if not ct['a'] % 2 and not ct['e'] % 2 and not ct['i'] % 2 and not ct['o'] % 2 and not ct['u'] % 2:
                return True
            return False
        biggestLen = 0
        #Implement sliding window here
        # for i in range(len(s)):
        #     for j in range(len(s)-1, i, -1):
        #         newStr = s[i:j+1]
        #         if countVowels(newStr):
        #             biggestLen = max(biggestLen, len(newStr))
        return biggestLen


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
