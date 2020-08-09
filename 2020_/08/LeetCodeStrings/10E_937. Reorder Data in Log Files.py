import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 93.95% of Python3 online submissions for Reorder Data in Log Files.
#Memory Usage: 14 MB, less than 30.28% of Python3 online submissions for Reorder Data in Log Files.

#["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def customsort(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=customsort)

#let# log
#dig# log
#1. letter log before digit log.
#2. letter logs ordered lexicographically w/o identifier. Only used in ties.
#3. dig log in order.
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         def sortLets(log):
#             id_, rest = log.split(" ", 1)
#             return (rest, id)
#         digs = []
#         lets = []
#         for s in logs:
#             if s.startswith("dig"):
#                 digs += s,
#             elif s.startswith("let"):
#                 lets += s,
#         lets.sort(key= sortLets)
#         res = lets + digs
#         return res

#012345
"let1 art"

s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))