import collections
import heapq

import numpy as np
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = collections.Counter(nums)
        return heapq.nlargest(k, occurences.keys(), occurences.get)

class Solution2:
    def topKFrequentFrequencies(self, nums: List[int], k: int) -> List[int]:
        occurences = collections.Counter(nums)
        return heapq.nlargest(k, occurences.values())

s= Solution()
print(s.topKFrequent([1,2,2,3,3,3], 2))
print(s.topKFrequent([1,1,1,2,2,3], 2))

print(s.topKFrequent([-1,-1], 2))

s = Solution2()
# 1-> 3 freq, 4: 3 freq. [3,3]
print(s.topKFrequentFrequencies([0,0,1,1,1,3,4,4,4],2))