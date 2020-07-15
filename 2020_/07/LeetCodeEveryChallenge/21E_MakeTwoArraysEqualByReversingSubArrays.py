import collections
import numpy as np
from typing import List

#thats crazy
#https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/discuss/660557/Python-One-Liner-with-Proof
# Here is and example on how to convert 3,4,1,2,3 to 1,2,3,3,4:
#
# 3,4,1,2,3 -> 1,2,3,3,4
# 3,4,1,2,3 -> 3,4,1 + 2,3 -> 1,4,3 + 2,3 -> 1 + 4,3,2,3
#
# 4,3,2,3 -> 2,3,3,4
# 4,3,2,3 -> 4,3,2 + 3 -> 2,3,4 + 3 -> 2 + 3,4,3
#
# 3,4,3 -> 3,3,4
# 3,4,3 -> 3 + 4,3 -> 3 + 4,3 -> 3 + 4,3
#
# 4,3 -> 3,4
# 4,3 -> 4,3 -> 3,4 -> 3 + 4
#
# 4 -> 4
# 4 -> 4 -> 4 -> 4
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if not arr:
            return []
        idx = arr.index(target[0])
        arr2 = arr[:idx +1][::-1] + arr[idx +1:]

        return [arr2[0]] + self.canBeEqual(target[1:],arr2[1:])

#
#67
#12
#(this isnt what they asked for)
class Solution2:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target)==sorted(arr)

print(Solution().canBeEqual([1, 2, 3, 3, 4],[3, 4, 1, 2, 3]))