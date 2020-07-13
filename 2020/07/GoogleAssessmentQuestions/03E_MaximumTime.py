import collections
import numpy as np
from typing import List
#Input: "?4:5?"
#Output: "14:59"


#23:59
class Solution:
    def maximumTime(self, s):
        sL = list(s)
        for i in range(len(s)-1,-1,-1):
            if sL[i] == '?':
                target = 9
                if i == 0:
                    if sL[1] <= '3':
                        target = '2'
                    else: target = '1'
                elif i == 1:
                    target = '3'
                elif i == 3:
                    target = '5'
                elif i == 4:
                    target = '9'
                sL[i] = target
        return ''.join(sL)

s = Solution()
print(s.maximumTime("?4:5?"))
print(s.maximumTime("??:??"))


