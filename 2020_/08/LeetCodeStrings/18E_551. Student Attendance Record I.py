import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 64.85% of Python3 online submissions for Student Attendance Record I.
#Memory Usage: 13.9 MB, less than 33.65% of Python3 online submissions for Student Attendance Record I.

class Solution:
    def checkRecord(self, s: str) -> bool:
        aCt = 0
        lCt_Continuous = 0
        for c in s:
            if c == 'A':
                aCt += 1
            if c == 'L':
                lCt_Continuous += 1
            else:
                lCt_Continuous = 0
            if aCt > 1 or lCt_Continuous > 2:
                return False
        return True

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("APPPPPLL"))