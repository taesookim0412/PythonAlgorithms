import collections
import numpy as np
from typing import List

# Runtime: 56 ms, faster than 22.26% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14.2 MB, less than 7.54% of Python3 online submissions for Unique Number of Occurrences.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cts = collections.Counter(arr)
        occs = set()
        for val in cts.values():
            if val in occs:
                return False
            occs.add(val)
        return True