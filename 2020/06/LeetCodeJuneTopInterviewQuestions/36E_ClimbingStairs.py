
#Runtime: 24 ms, faster than 92.01% of Python3 online submissions for Climbing Stairs.
#Memory Usage: 14 MB, less than 8.73% of Python3 online submissions for Climbing Stairs.

#Took me a lot more tries than I hoped :( still finished it solo though!

class Solution:
    memo = [0, 1, 2]
    def climbStairs(self, n: int) -> int:
        memo=self.memo
        if n==0: return memo[0]
        if n==1: return memo[1]
        if n==2: return memo[2]
        if n >= len(memo):
            memo.append(self.climbStairs(n-2) + self.climbStairs(n-1))
        return memo[n]


#Time limit exceeded it wouldnt be 46.9% acceptance if it didnt.
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        return self.climbStairs(n-2) + self.climbStairs(n-1)

s = Solution()
print(s.climbStairs(38))