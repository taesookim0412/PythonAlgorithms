#DP
from math import sqrt

#4796ms
#32.39% f runtime
#40.90% l mem


#pretty interesting problem.
#Many different possible approaches.
#DFS, DP, Lagrange's Four Square Theorem, None of which you'll probably understand when you first see it!
#TODO: Review Sum Of Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x for x in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, int(sqrt(i))+1):
                print(i, j,i-j*j, dp)

                dp[i] = min(dp[i], dp[i - j*j] + 1)
        print(dp)
        return dp[n]
s = Solution()
#print(s.numSquares(16))


#Recursive
class SolutionR:
    def numSquares(self, n: int) -> int:
        if n < 4: return n
        ct = 9999999
        for i in range(1, int(sqrt(n)+1)):
            print(n-i*i)
            ct = min(ct, self.numSquares(n-i*i) + 1)
        return ct
sr = SolutionR()
print(sr.numSquares(5))

#Tried
# class Solution:
#     def numSquares(self, n: int) -> int:
#         num = 1
#         squares = []
#         i = 1
#         while len(squares) == 0 or squares[-1] <= n:
#             squares.append(i*i)
#             i+=1
#         squares.pop()
#         print(squares)
#         lowest = 999999
#         for i in range(n):
#             for i in range(len(squares)-1, -1, -1):
#                 a = squares[i]
#                 if a + squares[-1-i] == n or a == n:
#                     return i+1
