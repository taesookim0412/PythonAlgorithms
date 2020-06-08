#Runtime: 32 ms, faster than 60.00% of Python3 online submissions for Power of Two.
#Memory Usage: 14 MB, less than 20.89% of Python3 online submissions for Power of Two.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==2 or n==1: return True
        while n > 1:
            n = n**1/2
            if n==2: return True
        return False

print(Solution().isPowerOfTwo(3))