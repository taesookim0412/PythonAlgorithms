import collections
import numpy as np
from typing import List





#Runtime: 32 ms, faster than 95.87% of Python3 online submissions for Add Strings.
#Memory Usage: 14 MB, less than 52.17% of Python3 online submissions for Add Strings.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #str to num
        #10
        maxLen = max(len(num1), len(num2))
        res = []
        placeHolder = 0
        num1 = list(num1)
        num2 = list(num2)
        for i in range(maxLen):
            n1 = (int(num1.pop())) if num1 else 0
            n2 = (int(num2.pop())) if num2 else 0
            res += (placeHolder + n1 + n2) % 10,
            placeHolder = (placeHolder + n1 + n2) // 10
        if placeHolder: res += placeHolder,
        return ''.join([str(x) for x in res])[::-1]

s = Solution()
#print(s.addStrings("0", "0"),'\n')
print(s.addStrings("10", "220"))
print(s.addStrings("9", "1"))
print(s.addStrings("19", "81"))
print(s.addStrings("119", "181"))


#Runtime: 124 ms, faster than 9.65% of Python3 online submissions for Add Strings.
#Memory Usage: 13.9 MB, less than 64.78% of Python3 online submissions for Add Strings.
class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        #str to num
        #10
        def strToNum(n):
            num_1 = 0
            place = 10 ** (len(n) - 1)
            for i in range(len(n)):
                c = int(n[i]) * (place)
                num_1 += c
                place//=10
            return num_1
        return str(strToNum(num1) + strToNum(num2))





#Runtime: 388 ms, faster than 5.24% of Python3 online submissions for Add Strings.
#Memory Usage: 14 MB, less than 38.13% of Python3 online submissions for Add Strings.
class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        #str to num
        #10
        def strToNum(n):
            num_1 = 0
            for i in range(len(n)):
                c = int(n[i]) * (10 ** (len(n) - i - 1))
                num_1 += c
            return num_1
        return str(strToNum(num1) + strToNum(num2))

