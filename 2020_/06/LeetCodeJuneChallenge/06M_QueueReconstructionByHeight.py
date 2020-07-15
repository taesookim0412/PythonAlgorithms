from typing import List
#Runtime: 96 ms, faster than 87.71% of Python3 online submissions for Queue Reconstruction by Height.
#Memory Usage: 14.4 MB, less than 15.42% of Python3 online submissions for Queue Reconstruction by Height.

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return p

print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))