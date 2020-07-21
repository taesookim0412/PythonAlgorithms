import collections
import math

import numpy as np
from typing import List

#N^2: Naive
#NLogN: Sort, Pass
#N: Dict (

#3: 3 1s
#[1,1,1]
#6: 4 1s
#[1,1,1,1]

# Runtime: 80 ms, faster than 7.11% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cts = collections.defaultdict(int)
        res = 0
        for num in nums:
            res += cts[num]
            cts[num] += 1
        return res


s =Solution()
print(s.numIdenticalPairs([1,1,1]))
print(s.numIdenticalPairs([1,1,1,1]))



#O(N^2) Naive
#O(1) memory
# Runtime: 76 ms, faster than 7.11% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs
s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))