from typing import List

#Runtime: 72 ms, faster than 60.34% of Python3 online submissions for Queries on a Permutation With Key.
#Memory Usage: 14 MB, less than 52.90% of Python3 online submissions for Queries on a Permutation With Key.

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(m, 0, -1)]
        res = []
        for i in range(len(queries)):
            qNum = queries[i]
            pos = p.index(qNum)
            res.append(len(p)-1-pos)
            p.remove(queries[i])
            p.append(queries[i])
        return res
s = Solution()
print(s.processQueries([3,1,2,1]
,5))