#Runtime: 68 ms, faster than 22.47% of Python3 online submissions for Bitwise AND of Numbers Range.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Bitwise AND of Numbers Range.
#05-25-2020_
#https://leetcode.com/problems/bitwise-and-of-numbers-range
#8266 / 8266 test cases passed.
#?


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m <= 0 <= n:
            return 0
        if n >= 2 * m:
            return 0
        bwA = m
        for i in range(m+1, n+1):
            bwA &= i
        return bwA

    def __init__(self):
        print(self.rangeBitwiseAnd(5, 7))
        print(self.rangeBitwiseAnd(0, 1))

Solution()