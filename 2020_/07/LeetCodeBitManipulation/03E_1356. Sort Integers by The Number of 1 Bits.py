import collections
import numpy as np
from typing import List
#Runtime: 72 ms, faster than 68.71% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
#Memory Usage: 13.8 MB, less than 86.25% of Python3 online submissions for Sort Integers by The Number of 1 Bits.

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        data = collections.defaultdict(list)
        res = []
        for i in range(len(arr)):
            numberOfOnes = str(bin(arr[i])).count('1')
            data[numberOfOnes] += arr[i],
        for key, val in sorted(data.items()):
            print(key,val)
            res += val
        return res
s = Solution()
print(s.sortByBits([0,1,2,3,4,5,6,7,8]))
print(s.sortByBits([10,100,1000,10000]))