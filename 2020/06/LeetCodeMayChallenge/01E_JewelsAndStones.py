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
