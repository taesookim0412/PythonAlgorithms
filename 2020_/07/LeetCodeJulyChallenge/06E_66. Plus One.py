import collections
import numpy as np
from typing import List

#32ms
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for i, a in enumerate(reversed(digits)):
            num += a*10**i
        return list(str(num))

s = Solution()
print(s.plusOne([2,2,4]))


#32ms (70+% faster)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(x) for x in digits]))
        num += 1
        return list(str(num))