import collections
import numpy as np
from typing import List

#The formal way is to prove by induction, which you can read up yourself if you are interested.
# Here is a helpful tip to quickly prove the correctness of your binary search algorithm during an
# interview. We just need to test an input of size 2.
# Check if it reduces the search space to a single element (which must be the answer) for both of the
# scenarios above. If not, your algorithm will never terminate.


#Runtime: 48 ms, faster than 10.30% of Python3 online submissions for First Bad Version.
#Memory Usage: 13.7 MB, less than 78.39% of Python3 online submissions for First Bad Version.
#https://leetcode.com/problems/first-bad-version/discuss/730332/Binary-search-solution-wvideo-whiteboard-explanation
class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l < r:
            mid = l + (r - l) // 2
            print(l,r,mid)
            if isBadVersion(mid) is False:
                l = mid + 1
            else:
                r = mid
        return l

def isBadVersion(num):
    return num > 26

s= Solution()
print(s.firstBadVersion(30))

