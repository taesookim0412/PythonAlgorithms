import collections
import numpy as np
from typing import List

#Runtime: 28 ms, faster than 81.91% of Python3 online submissions for Detect Capital.
#Memory Usage: 13.8 MB, less than 69.68% of Python3 online submissions for Detect Capital.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppers = 0
        for i in range(len(word)):
            if word[i].isupper():
                uppers += 1
        if uppers == len(word):
            return True
        if uppers == 0:
            return True
        if uppers == 1 and word[0].isupper():
            return True
        return False