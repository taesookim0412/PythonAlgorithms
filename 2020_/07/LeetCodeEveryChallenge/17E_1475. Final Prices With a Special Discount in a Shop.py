import collections
import numpy as np
from typing import List

#Runtime: 72 ms, faster than 43.04% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Final Prices With a Special Discount in a Shop.

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discs = []
        for i in range(len(prices)):
            discd = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    discs.append(prices[i]-prices[j])
                    discd = True
                    break
            if not discd:
                discs.append(prices[i])

