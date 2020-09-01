import collections
import numpy as np
from typing import List

A = {'(':3, ')':3}
# print([list(collections.Counter(A).values())])
# print(list(map(lambda lst: len(lst) == 2 and lst[0] == lst[1] == 3,[list(collections.Counter(A).values())]))[0])


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