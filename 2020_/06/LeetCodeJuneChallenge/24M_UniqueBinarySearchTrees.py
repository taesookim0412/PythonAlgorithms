import itertools

#Runtime: 28 ms, faster than 76.14% of Python3 online submissions for Unique Binary Search Trees.
#Memory Usage: 13.9 MB, less than 24.52% of Python3 online submissions for Unique Binary Search Trees.

#These for loops produce the same output as catalan's number.
class SolutionI:
    def numTrees(self, n:int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]




from math import factorial

#92.98% faster
#46.96% less mem
class Solution:
    def numTrees(self, n: int) -> int:
        return int(factorial(2*n)/(factorial(n+1) * factorial(n)))
#n==3 : 5 uniqu`e
#1==1, 2== 2, 3==5
#n! = n * n-1
#1
#wrong this entire time it's the catalan factorial
#2n!/(n+1)!*n!)
s = SolutionI()
print(s.numTrees(3))
