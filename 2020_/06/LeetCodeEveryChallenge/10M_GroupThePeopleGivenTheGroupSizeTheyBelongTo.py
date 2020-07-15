import collections
from typing import List
#Runtime: 92 ms, faster than 24.62% of Python3 online submissions for Group the People Given the Group Size They Belong To.
#Memory Usage: 14 MB, less than 32.06% of Python3 online submissions for Group the People Given the Group Size They Belong To.

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        grps = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            grps[groupSizes[i]] += i,
        for a in grps:
            b = grps[a]
            times = len(b)// a
            for i in range(times):
                res += [b[len(b)-(i+1)*a:len(b)-(i)*a]]
        return res

s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))
