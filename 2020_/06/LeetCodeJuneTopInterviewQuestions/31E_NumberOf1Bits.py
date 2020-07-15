#Runtime: 32 ms, faster than 54.60% of Python3 online submissions for Number of 1 Bits.
#Memory Usage: 13.8 MB, less than 71.68% of Python3 online submissions for Number of 1 Bits.


#BitAnd then bitshift mask.
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        ones = 0
        for i in range(32):
            if n & mask != 0:
                ones += 1
            mask <<= 1
            #print(n&mask)
            #print(mask)
        return ones
#TODO: Study bit trick (Solution #2)

s = Solution()
print(s.hammingWeight(0o0000000000000000000000000001011))
