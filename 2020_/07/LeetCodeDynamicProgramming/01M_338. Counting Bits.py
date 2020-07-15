import collections
import numpy as np
from typing import List

#Runtime: 136 ms, faster than 18.09% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.7 MB, less than 55.54% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0 for _ in range(num+1)]
        for i in range(num+1):
            res[i] = res[i>>1] + (i&1)
            #res[i] = (res[i//2] + i%2)
        return res


class Solution2:
    def countBits(self, num: int) -> List[int]:
        res = []
        mask = 1
        for i in range(num + 1):
            ct = 0
            for j in range(32):
                if mask & i != 0:
                    ct += 1
                mask <<= 1
            res.append(ct)
            mask = 1
        print(res[:10])
        print(res[10:20])
        return res
s = Solution()
print(s.countBits(5))