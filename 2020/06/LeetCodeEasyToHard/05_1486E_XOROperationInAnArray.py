#Runtime: 28 ms, faster than 82.88% of Python3 online submissions for XOR Operation in an Array.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for XOR Operation in an Array.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*i for i in range(n)]
        out = nums[0]
        for i in range(1,len(nums)):
            out^=nums[i]
        return out


s = Solution()
print(s.xorOperation(5,0))
#8
print(s.xorOperation(4,3))