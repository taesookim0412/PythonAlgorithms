import collections
import numpy as np
from typing import List

#Runtime: 40 ms, faster than 51.84% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.3 MB, less than 11.40% of Python3 online submissions for Generate Parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, L,R):
            if len(s) == 2*n:
                res.append(s)
                return
            if L < n:
                backtrack(s + '(', L + 1, R)
            if R < L:
                backtrack(s + ')', L, R+1)
        backtrack("", 0,0)
        return res




A = {'(':3, ')':3}
# print([list(collections.Counter(A).values())])
# print(list(map(lambda lst: len(lst) == 2 and lst[0] == lst[1] == 3,[list(collections.Counter(A).values())]))[0])
import time
ct = time.time()
nums = [i for i in range(999999)]
print(time.time() - ct)
ct2 = time.time()
nums2 = [nums.copy()]
print(time.time() - ct2)
ct2 = time.time()
nums2 = [nums]
print(time.time() - ct2)
ct2 = time.time()
nums4 = [nums]
print(time.time() - ct2)
print(len(nums4[0]))
nums.append(1)
print(len(nums4[0]))

# Runtime: 160 ms, faster than 5.17% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.1 MB, less than 54.24% of Python3 online submissions for Generate Parentheses.
class Solution:


    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(A=[]):
            if len(A) == 2*n:
                if list(map(valid, [A]))[-1]:
                    res.append(''.join(A))
            else:
                A += '(',
                generate(A)
                A.pop()
                A += ')'
                generate(A)
                A.pop()
        def valid(A):
            balance = 0
            ss = {'(': 1, ')': -1}
            for c in A:
                balance += ss[c]
                if balance < 0:
                    return False
            return balance == 0

        generate()
        return res

print(Solution.generateParenthesis('_',3))