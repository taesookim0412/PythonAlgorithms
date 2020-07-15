import collections
import numpy as np
from typing import List

#Runtime: 112 ms, faster than 85.71% of Python3 online submissions for Find Smallest Letter Greater Than Target.
#Memory Usage: 13.9 MB, less than 82.21% of Python3 online submissions for Find Smallest Letter Greater Than Target.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]: return letters[0]
        l = 0
        r = len(letters)-1
        while l < r:
            mid = l + (r-l)//2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l]

s = Solution()
#c
print(s.nextGreatestLetter(["c","f","j"], "a"))
#f
print(s.nextGreatestLetter(["c","f","j"], "c"))
#f
print(s.nextGreatestLetter(["c","f","j"], "d"))
#j
print(s.nextGreatestLetter(["c","f","j"], "g"))
#c
print(s.nextGreatestLetter(["c","f","j"], "k"))
#n
print(s.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"e"))

