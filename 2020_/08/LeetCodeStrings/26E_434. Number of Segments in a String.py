import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 60.73% of Python3 online submissions for Number of Segments in a String.
#Memory Usage: 13.8 MB, less than 47.23% of Python3 online submissions for Number of Segments in a String.

class Solution:
    def countSegments(self, s: str) -> int:
        return len(list(filter(None, s.split(' '))))