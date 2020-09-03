import collections
import numpy as np
from typing import List

#
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ct = 0
#         for i in range(len(s)):
#             ct += 1
#             S1 = s[i]
#             for j in range(i + 1, len(s)):
#                 S1 += s[j]
#                 # print(S1)
#                 if S1 == S1[::-1]:
#                     ct += 1
#                 elif j != len(s)-1 and S1[-2] != s[j+1]:
#                     break
#         return ct

# abba
# ab ba
# aaa

#Runtime: 480 ms, faster than 24.95% of Python3 online submissions for Palindromic Substrings.
#Memory Usage: 13.7 MB, less than 88.46% of Python3 online submissions for Palindromic Substrings.
class Solution2:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        S = ""
        for i in range(len(s)):
            ct += 1
            S1 = s[i]
            for j in range(i + 1, len(s)):
                S1 += s[j]
                # print(S1)
                if S1 == S1[::-1]:
                    ct += 1
            # for j in range(i - 1, -1, -1):
            #     S1 += s[j]
            #     if S2 == S2[::-1]:
            #         ct +=1
            #     else:
            #         break
            # for j in range(i+1, len(s)):
            #     S2 += s[j]
            #     if S2 == S2[::-1]:
            #         ct += 1
            #     else:
            #         break
        return ct

s = Solution()
print(s.countSubstrings("aba"))