import collections
import numpy as np
from typing import List

#Runtime: 1232 ms, faster than 16.55% of Python3 online submissions for Sort Integers by The Power Value.
#Memory Usage: 13.9 MB, less than 60.61% of Python3 online submissions for Sort Integers by The Power Value.

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [i for i in range(lo, hi+1)]
        power = nums.copy()
        for i in range(hi+1-lo):
            steps = 0
            while power[i] != 1:
                if power[i] & 1:
                    power[i] = power[i] * 3 + 1
                elif power[i] & 1 == 0:
                    power[i] //= 2
                steps += 1
            power[i] = (steps, nums[i])
        #power[2], power[3] = power[3], power[2]
        #power.sort(key=lambda x: x[0])
        print(power)
        #kth: power[k-1]
        return power[k-1][1]
s = Solution()
print(s.getKth(12,15,2))