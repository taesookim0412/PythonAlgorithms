#No + or - Operators

#Couldn't come up with this one myself
#Runtime: 28 ms, faster than 73.76% of Python3 online submissions for Sum of Two Integers.
#Memory Usage: 13.8 MB, less than 71.88% of Python3 online submissions for Sum of Two Integers.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])

sol = Solution()
print(sol.getSum(4, 7))

#-1
print(sol.getSum(1, -2))
#-3
print(sol.getSum(-1, -2))
#3
print(sol.getSum(1, 2))
