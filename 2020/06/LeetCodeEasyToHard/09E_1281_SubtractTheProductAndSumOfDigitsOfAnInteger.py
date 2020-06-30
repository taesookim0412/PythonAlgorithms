#Runtime: 36 ms, faster than 18.79% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
#Memory Usage: 13.8 MB, less than 59.22% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = []
        while n > 0:
            num += n % 10,
            n //= 10
        prod = 1
        sum = 0
        for i in range(len(num)-1, -1, -1):
            numb = num[i]
            prod *= numb
            sum += numb
        return prod - sum
s = Solution()
#1
print(s.subtractProductAndSum(32))