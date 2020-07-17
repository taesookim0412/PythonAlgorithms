import collections
import numpy as np
from typing import List


#Hashmap solution,
# Runtime: 816 ms, faster than 53.00% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.2 MB, less than 56.38% of Python3 online submissions for Find the Town Judge.


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustedByCt = collections.defaultdict(int)
        trustsGiven = collections.defaultdict(int)
        for i in range(len(trust)):
            trustedByCt[trust[i][1]] += 1
            trustsGiven[trust[i][0]] += 1

        for i in range(1, N + 1):
            # print(trustedByCt[i], trustsGiven[i])
            if trustedByCt[i] == N - 1 and trustsGiven[i] == 0:
                return i
        return -1