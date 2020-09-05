import collections
import numpy as np
from typing import List

import numpy as np


# Runtime: 144 ms, faster than 70.11% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 13.9 MB, less than 55.34% of Python3 online submissions for Palindromic Substrings.
class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        for i in range(2*len(s) - 1):
            L = i // 2
            R = L + i % 2
            while L >= 0 and R <= len(s) - 1 and s[L] == s[R]:
                ct += 1
                L -= 1
                R += 1
        return ct

class SolutionNp:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        for i in range(len(s)):
            ct += 1
            S1 = np.asarray(s[i])
            errors = 0
            for j in range(i + 1, len(s)):
                #appendndarray
                #A copy of arr with values appended to axis. Note that append does not occur in-place: a new array is allocated and filled. If axis is None, out is a flattened array.
                S1 = np.append(S1, s[j])
                if np.all(S1 == np.flip(S1)):
                    ct += 1
                elif errors < 2:
                    errors += 1
                elif errors > 2:
                    break
        return ct

#Runtime: 504 ms, faster than 22.95% of Python3 online submissions for Palindromic Substrings.
#Memory Usage: 13.9 MB, less than 66.05% of Python3 online submissions for Palindromic Substrings.
class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = 0
        for i in range(len(s)):
            ct += 1
            S1 = s[i]
            errors = 0
            for j in range(i + 1, len(s)):
                S1 += s[j]
                # print(S1)
                if S1 == S1[::-1]:
                    ct += 1
                elif errors < 10:
                    errors += 1
                elif errors > 10:
                    break
        return ct


# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ct = 0
#         a_s = ""
#         for i, c in enumerate(s):
#             a_s += s
#             ct += 1
#             L, R = i-1, i+1
#             a_s2 = a_s
#             while L >= 0 and R <= len(s) -1:
#                 a_s2 += s[L]
#                 if a_s2 == a_s2[::-1]:
#                     ct += 1
#                 else: a_s2 -= s[L]
#                 a_s2 += s[R]
#                 if a_s2 == a_s2[::-1]:
#                     ct += 1
#                 else: a_s2 -= s[R]
#                 L -= 1
#                 R += 1
#         return ct
s = Solution()
print(s.countSubstrings("aaa"))

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

#64

print(s.countSubstrings("bbccaacacdbdbcbcbbbcbadcbdddbabaddbcadb"))
#0.0009999275207519531
#1*10^-3
np_s = SolutionNp()
import time
curr2 = time.time()
print(np_s.countSubstrings("bbccaacacdbdbcbcbbbcbadcbdddbabaddbcadb"))
print('t2: ', (time.time() - curr2) * 10**3)

