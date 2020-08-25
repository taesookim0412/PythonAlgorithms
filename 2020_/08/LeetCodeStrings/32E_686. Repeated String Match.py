import collections
import numpy as np
from typing import List

#Runtime: 288 ms, faster than 13.11% of Python3 online submissions for Repeated String Match.
#Memory Usage: 13.9 MB, less than 68.36% of Python3 online submissions for Repeated String Match.

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = len(B)//len(A)
        for i in range(3):
            mult = (i+times)
            newStr = A * mult
            #print(newStr)
            if newStr.find(B) != -1:
                return times + i
        return -1


#Yeah not gonna engineer a 200 line mess for no reason
#Assumes len(B) > len(A)
class Solution2:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if A * (len(B)//len(A)) == B:
            return len(B)//len(A)
        start = B.find(A)
        times = 0
        offset = 0
        if start > 0:
            times += 1
            offset += start
        #Returns an index value
        end = B.rfind(A)
        #Add the length - Now at first element after Indx
        end += len(A)
        #If not last element + 1:
        if -1 < end < len(B):
            times += 1
            #Add Len(B) + 1 - 1 - end
            #(Last Element null terminator minus one for index minus end index)
            # print(len(B) + 1 - end)
            offset += len(B) - end
        # print(offset)
        times += (len(B)-offset)//len(A)
        # print(times)
        return times if (A*times).find(B) > -1 else -1

s = Solution2()

#1
print(s.repeatedStringMatch("aa","a"))
#2
print(s.repeatedStringMatch("a","aa"))
#2
print(s.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab","ba"))

#3
print(s.repeatedStringMatch("abcd","cdabcdab"))
#4
print(s.repeatedStringMatch("abc","cabcabca"))