import collections
import numpy as np
from typing import List
import bisect


nums = [1, 2,2,2, 3, 4, 5, 6]
left = bisect.bisect_left(nums, 2, 0)
right = bisect.bisect_right(nums, 2, 0)

print(left,right)