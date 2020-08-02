import collections
import numpy as np
from typing import List


# nd st
#Runtime: 24 ms, faster than 97.92% of Python3 online submissions for Reformat Date.
#Memory Usage: 13.7 MB, less than 80.77% of Python3 online submissions for Reformat Date.
class Solution:
    def reformatDate(self, date: str) -> str:
        res = []
        nd = date.find("nd")
        st = date.find("st")
        rd = date.find("rd")
        th = date.find("th")

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        idx = 0
        if nd != -1:
            idx = nd
        elif st != -1:
            idx = st
        elif rd != -1:
            idx = rd
        elif th != -1:
            idx = th
        day = int(date[:idx])
        day = str(day)
        if len(day)==1:
            day = "0" + day

        #month starts at idx + 3
        monthStr = date[idx+3:idx+6]
        print(monthStr)
        month = months.index(monthStr) + 1
        month = str(month)
        if len(month) == 1:
            month = "0" + month
        yearStr = date[idx+7:]
        print(yearStr)
        res += yearStr, month, day,
        return '-'.join(res)


s = Solution()
print(s.reformatDate("20th Oct 2052"))