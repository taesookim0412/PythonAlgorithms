import collections
import numpy as np
from typing import List

# Runtime: 32 ms, faster than 93.80% of Python3 online submissions for Find And Replace in String.
# Memory Usage: 14.1 MB, less than 5.06% of Python3 online submissions for Find And Replace in String.

class Solution:

    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = list(sorted([[i, x, y]
         for i, x, y in zip(indexes, sources, targets)]))
        #print(res)
        differences = [len(target) - len(src) for _, src, target in res]
        offset_sum = 0
        for entry, z in zip(res, differences):
            i, x, y = entry
            new_i = i + offset_sum

            #Find: 93.8%
            findRes = S.find(x, new_i, new_i + len(x))
            #String slice: 21.69%
            #findRes = S[new_i: new_i+ len(x)] == x
            if findRes:
                offset_sum += z
                S = S[:new_i] + y + S[new_i + len(x):]
            #print(S)
        return S

        # for i, x, y, z in zip(indexes, sources, targets, differences):
        #     new_i = i + offset_sum
        #     findRes = S.find(x, new_i)
        #     if findRes == new_i:
        #         offset_sum += z
        #         S = S[:new_i] + y + S[new_i + len(x):]
        # return S





s = Solution()
print(s.findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"]))
print(s.findReplaceString("abcd", [1,2], ["b","cd"], ["eee","ffff"]))
#"vbfrssozp"
print(s.findReplaceString("vmokgggqzp",
[3,5,1],
["kg","ggq","mo"],
["s","so","bfr"]))

#vbfkqqqzp
#

