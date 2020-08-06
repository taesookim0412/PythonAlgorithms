import collections
import numpy as np
from typing import List

# ?
class Solution:
    def rotatedDigits(self, N: int) -> int:
        # 4 in the range 1 to 10
        res = 0
        tens = N // 10
        ones = N % 10
        tensNums = tens * 4

        res += tensNums

        goods = [2, 5, 6, 9]
        for i in range(len(goods)):
            if goods[i] <= ones:
                res += 1
        return res



