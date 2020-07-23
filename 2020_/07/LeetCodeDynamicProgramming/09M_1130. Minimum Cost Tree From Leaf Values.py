import collections
import numpy as np
from typing import List


#It's incorrect

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr)==2: return arr[0]*arr[1]
        dp = [0 for _ in range(len(arr)+3)]
        dpReverse = dp.copy()
        dp[1], dp[2], dp[3] = arr[0],arr[1],arr[2]
        dpReverse[3], dpReverse[2], dpReverse[1] = arr[0],arr[1],arr[2]

        dp[4] = dp[1]*dp[2]
        dpReverse[4] = dpReverse[1]*dpReverse[2]
        for i in range(5, len(arr)+3):
            dp[i] = dp[i-1] + dp[i-4]*dp[i-2]
            dpReverse[i] = dpReverse[i - 1] + dpReverse[i - 4] * dpReverse[i - 2]
        return min(dp[-1], dpReverse[-1])

s= Solution()
print(s.mctFromLeafValues([1,2,3]))
