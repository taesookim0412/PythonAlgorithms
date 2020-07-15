import collections
import numpy as np
from typing import List

def binarysearch(n, target):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r)>>1
        print(l, r,mid)
        if mid > target:
            r = mid-1
        elif mid < target:
            l = mid+1
        if mid == target:
            return target


print(binarysearch(25,7))