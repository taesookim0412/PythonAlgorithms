import itertools

#!!!!!!!TODO tomorrow morning: memorize the forloops
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
s = Solution()
print(s.numTrees(3))
