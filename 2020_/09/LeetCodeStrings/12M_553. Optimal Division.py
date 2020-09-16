import collections
import numpy as np
from typing import List

#1/93

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        #max number with one paren
        nums.sort(reverse=True)
        res = str(f"{nums[0]}/(")
        for i in range(1, len(nums)):
            num = nums[i]
            if num >= 1:
                res += str(f"{nums[i]}/")
        res = res[:-1] + ")"
        if num < 1:
            for j in range(i, len(nums)):
                res += str(f"/{nums[j]}")
        return res