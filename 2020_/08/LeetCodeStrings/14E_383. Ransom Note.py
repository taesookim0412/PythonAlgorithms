import collections
import numpy as np
from typing import List
#Runtime: 52 ms, faster than 73.69% of Python3 online submissions for Ransom Note.
#Memory Usage: 14.1 MB, less than 32.75% of Python3 online submissions for Ransom Note.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCt = collections.Counter(magazine)
        ranCt = collections.Counter(ransomNote)
        #doesnt work for nonexistant ranCt keys
        #cts = magCt - ranCt
        #Solution 2:
        #cts = {key: magCt[key] - ranCt[key] for key in ranCt.keys()}
        #Solution 1:
        cts = ranCt - magCt
        for x in cts.values():
            if x > 0:
                return False
        return True