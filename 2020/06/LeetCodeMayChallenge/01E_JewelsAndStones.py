#Runtime: 28 ms, faster than 76.63% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 13.7 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewls = set()
        ct = 0
        for i in range(len(J)):
            jewls.add(J[i])
        for i, a in enumerate(S):
            if a in jewls:
                ct += 1
        return ct
