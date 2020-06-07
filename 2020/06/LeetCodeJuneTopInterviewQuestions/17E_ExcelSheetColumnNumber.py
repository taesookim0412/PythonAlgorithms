#Runtime: 32 ms, faster than 62.72% of Python3 online submissions for Excel Sheet Column Number.
#Memory Usage: 13.7 MB, less than 89.43% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        tot = 0
        for i in range(0, len(s)):
            tot += 26 ** i * (ord(s[i]) - 64)
        return tot
