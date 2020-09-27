import collections
import numpy as np
from typing import List


class Solution:
    #abcaa
    # def reorganizeString(self, S: str) -> str:
    #     wordCt = collections.Counter(S)
    #     if len(wordCt)  <= len(S) / 2:
    #         return ''
    #     res = ['' for _ in range(len(S))]
    #     indx = 0
    #     while indx != len(S):
    #         dels = []
    #         for word, ct in wordCt.items():
    #             res[indx] = word
    #             if ct == 1:
    #                 dels += word
    #             else:
    #                 wordCt[word] -= 1
    #             indx += 1
    #             if indx == len(S):
    #                 break
    #         for entry in dels:
    #             del wordCt[entry]
    #     return ''.join(res)



s = Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("aaab"))
print(s.reorganizeString("aaabc"))