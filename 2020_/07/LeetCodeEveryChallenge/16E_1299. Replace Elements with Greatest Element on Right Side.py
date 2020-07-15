import collections
import numpy as np
from typing import List

#Runtime: 184 ms, faster than 45.02% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
#Memory Usage: 14.7 MB, less than 81.08% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        dp = [0 for _ in range(len(arr))]
        highst = arr[-1]
        #The highest to the right of 18 is 6 therefore 18 gets replaced by 6.
        #Thus we need another additional step dp array before it records its highest.
        #That means the resultant array would return the correct value.
        for i in range(len(arr)-1, -1, -1):
            dp[i] = highst
            highst = max(highst, arr[i])
        print(dp, arr)
        for i in range(len(arr)):
            arr[i] = dp[i]
        arr[-1] = -1
        return arr

print(Solution().replaceElements([17,18,5,4,6,1]))