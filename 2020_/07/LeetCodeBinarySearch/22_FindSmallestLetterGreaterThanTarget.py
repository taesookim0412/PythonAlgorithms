import collections
import numpy as np
from typing import List

#Find the closest element larger than target
class Solution:
    def nextGreatestLetter(self, letters:List[str], target:str):
        l, r = 0, len(letters) - 1
        while l < r:
            mid = l + (r - l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l] if letters[l] > target else letters[0]
s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], "a"))
print(s.nextGreatestLetter(["a", "b"], "z"))
print(s.nextGreatestLetter(["c","f","j"], "c"))


