import collections
import numpy as np
from typing import List


#wrong
class Solution:
    def isValid(self, s: str) -> bool:
        enders = {'(':')',
                  '{':'}',
                  '[':']'}
        res = []
        i=0
        while i < len(s):
            #get enders
            if s[i] not in enders:
                return False
            while s[i] in enders:
                res += enders[s[i]],
                if i == len(s) - 1:
                    break
                i+=1
            res = res[::-1]
            print(s[:i] + ''.join(res), s[:i*2])
            print(i*2, len(s))
            if len(s) < i*2 or s[:i] + ''.join(res) != s[:i*2]:
                return False
            res = []
            s = s[i*2:]
            i = 0
        return True

s = Solution()
print(s.isValid('()'))
print(s.isValid('()[]'))
print(s.isValid('(){}'))
print(s.isValid('(({{}}))'))
print(s.isValid('({}){[]}'))

#rip
print(s.isValid("(([]){})"))


print("False Results:")
print(s.isValid('(([))'))
print(s.isValid('(([])))'))
print(s.isValid('([)[(]'))