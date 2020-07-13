import collections
import numpy as np
from typing import List

#"abcd aabc bd"
#"aaa aa"
#[3,2]
#3 strings with frequency smaller than B_0,
#2 strings with frequency smaller than B_1


class Solution:
    def compareStrings(self, a:List[str], b:List[str]):
        res = [0 for _ in range(len(b))]
        a.sort()
        for i in range(len(b)):
            a = b[i]
            l = 0
            r = len(a)-1
            while l < r:
                mid = l + (r-l)//2
                if a[mid] <= a:
                    l = mid + 1
                else:
                    r = mid
            res[i] = l + 1

        return res


#O(N^2) Runtime
class Solution2:
    def compareStrings(self, a:List[str], b:List[str]):
        res = [0 for _ in range(len(b))]
        for i in range(len(b)):
            a = b[i]
            for j in a:
                if j < a:
                    res[i] += 1
        return res


s = Solution()
print(s.compareStrings(["abcd","aabc","bd"],["aaa","aa"]))