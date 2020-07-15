#TODO:
# binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left+right)//2
            #(k(k+1))/2 coins
            curr = mid * (mid+1)
            print(mid,curr)

            if curr == n:
                return mid
            if n < curr:
                right = mid -1
            else:
                left = mid + 1
        return right

#iteration
class Solution2:
    def arrangeCoins(self, n: int) -> int:
        if n==0: return 0
        memo = []
        stack = [1]
        n-=1
        while len(stack) > 0:
            memo += stack.pop(),
            print(n, memo[-1])
            if n > memo[-1]:
                stack += memo[-1] + 1,
                n-= stack[-1]
        return len(memo)
s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))