import collections
import numpy as np
from typing import List

# Center an array based on its pivot.
# Input:
# prods: List of products centered about 0
# k: index of element that is being centered
#
# Output:
# Center the array about the pivot index.
# Example:
#
# Input:
# [-1,0,1],0
# Output:
# [0,1,2]
#
# Input:
# [-1,0,1,2,3], 3
# Output:
# [-3,-2,-1,0,1]
#
# Input:
# [-4,-3,-2,-1,0], 0
# Output:
# [0,1,2,3,4]

class Solution:
    def centerAboutPivot(self, prods, target):
        diff = prods[target]
        for i in range(len(prods)):
            prods[i] -= diff
        return prods

s = Solution()
print(s.centerAboutPivot([-1,-0,1], 0))
print(s.centerAboutPivot([-1,0,1,2,3], 3))
print(s.centerAboutPivot([-4,-3,-2,-1,0], 0))