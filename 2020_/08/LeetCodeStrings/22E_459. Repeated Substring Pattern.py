import collections
import numpy as np
from typing import List
import math


#Runtime: 92 ms, faster than 54.07% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 13.9 MB, less than 42.42% of Python3 online submissions for Repeated Substring Pattern.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1: return False
        sList = list(s)
        ls = list(s[:math.ceil(len(s)/2)])
        for i in range(len(ls) - 1, -1, -1):
            #print(ls)
            #i+1 or len(ls)
            if (len(s)/len(ls)).is_integer():
                times = len(s) // len(ls)
                ls2 = ls * times
                if ls2 == sList:
                    return True
                #print(ls2, "\n", sList)
            ls.pop()
        return False

#Runtime: 104 ms, faster than 50.51% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 13.9 MB, less than 42.42% of Python3 online submissions for Repeated Substring Pattern.
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1: return False
        sList = list(s)
        ls = list(s[:math.ceil(len(s)/2)])
        for i in range(len(ls) - 1, -1, -1):
            #print(ls)
            #i+1 or len(ls)
            if len(s)%len(ls) == 0:
                times = len(s) // len(ls)
                ls2 = ls * times
                if ls2 == sList:
                    return True
                #print(ls2, "\n", sList)
            ls.pop()
        return False

#Runtime: 440 ms, faster than 9.59% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14 MB, less than 30.69% of Python3 online submissions for Repeated Substring Pattern.

class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1: return False
        sList = list(s)
        ls = list(s[:math.ceil(len(s)/2)])
        for i in range(len(ls) - 1, -1, -1):
            #print(ls)
            #i+1 or len(ls)
            if len(s)%len(ls) == 0:
                times = len(s) // len(ls)
                ls2 = []
                ls2 += [item for _ in range(times) for item in ls]
                if ls2 == sList:
                    return True
                #print(ls2, "\n", sList)
            ls.pop()
        return False

#Our termination takes too long, reverse the loop
#Runtime: 84 ms, faster than 55.68% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14.1 MB, less than 12.03% of Python3 online submissions for Repeated Substring Pattern.
class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = ""
        rs = list(s)[::-1]
        for i in range(1, (len(s)//2)+1):
            ls += rs.pop()
            #if i rem len
            if len(s)%i == 0:
                times = len(s) // i
                ls2 = ls * times
                if ls2 == s:
                    return True
        return False

#Runtime: 40 ms, faster than 82.89% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14.1 MB, less than 12.65% of Python3 online submissions for Repeated Substring Pattern.

class Solution99:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2, 0, -1):
            if len(s)%i == 0:
                ls = s[:i]
                if ls * (len(s)//i) == s:
                    return True


#Runtime: 872 ms, faster than 6.48% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 13.9 MB, less than 40.33% of Python3 online submissions for Repeated Substring Pattern.

class Solution4:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = ""
        rs = list(s)[::-1]
        for i in range(len(s)//2):
            ls += rs.pop()
            ls2 = ls
            while len(ls2) <= len(s) and (len(s)/len(ls)).is_integer():
                if len(ls2) == len(s):
                    if ls2 == s:
                        return True
                    break
                ls2 += ls
        return False

s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("ababab"))
print(s.repeatedSubstringPattern("babbabbabbabbab"))
print(s.repeatedSubstringPattern("zzz"))



print(s.repeatedSubstringPattern("a"))
print(s.repeatedSubstringPattern("abcdabra"))





#testStr = "sssss"
#print(len(testStr)//2)
#print(testStr[:math.ceil(len(testStr)/2)])