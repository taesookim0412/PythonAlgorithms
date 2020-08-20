import collections
import numpy as np
from typing import List
import itertools

#Runtime: 36 ms, faster than 56.58% of Python3 online submissions for Long Pressed Name.
#Memory Usage: 13.9 MB, less than 36.63% of Python3 online submissions for Long Pressed Name.

class Solution:
    def isLongPressedName(self, name:str, typed:str):
        grps_A = [(a, len(list(b))) for a, b in itertools.groupby(name)]
        grps_B = [(a, len(list(b))) for a, b in itertools.groupby(typed)]
        if len(grps_A) != len(grps_B):
            return False
        for a, b in zip(grps_A, grps_B):
            if a[0] != b[0] or a[1] > b[1]:
                return False
        return True

#Runtime: 60 ms, faster than 10.25% of Python3 online submissions for Long Pressed Name.
#Memory Usage: 13.6 MB, less than 97.52% of Python3 online submissions for Long Pressed Name.

class Solution1:
    def isLongPressedName(self, name:str, typed: str):
        nI, tI = 0, 0
        while tI < len(typed) and nI < len(name):
            if typed[tI] != name[nI]:
                return False
            repeats = 0
            while tI < len(typed) and nI < len(name) and typed[tI] == name[nI]:
                tI += 1
                repeats += 1
            while nI < len(name) and repeats > 0 and typed[tI - 1] == name[nI]:
                nI += 1
                repeats -= 1
        return True if nI == len(name) and tI == len(typed) else False

#GroupBy Solution would be nice

#12011
#waada
#130011
#waaada

# Runtime: 60 ms, faster than 10.28% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 14 MB, less than 16.34% of Python3 online submissions for Long Pressed Name.

class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def numify(s):
            res = [0] * (len(s))
            idx = 0
            ct = 0
            lastChar = s[0]
            for i in range(len(s)):
                if s[i] == lastChar:
                    res[idx] += 1
                else:
                    idx = i
                    res[idx] = 1
                    lastChar = s[i]
            return res
        namedNums, typedNums = numify(name), numify(typed)
        #[1,1,1,1]
        #[1,1,1,2,0]
        nI, tI = 0,0
        # print(namedNums, typedNums)
        for i in range(len(typed)):
            #if nI out of range
            if nI >= len(name): return False
            # print(nI, tI)
            if typedNums[tI] != 0:
                if typedNums[tI] < namedNums[nI] or typed[tI] != name[nI]:
                    # print(typed[tI], name[nI])
                    return False
                nI -= (typedNums[tI] - namedNums[nI])
            nI +=1
            tI += 1
        if nI != len(name):
            return False
        return True

s = Solution()
print(s.isLongPressedName("wada", "waada"))
print(s.isLongPressedName("wada", "waada"))
print(s.isLongPressedName("mata", "maaattta"))
print(s.isLongPressedName("teelee", "tteelee"))

print('False Results')
print(s.isLongPressedName("yomata", "youmata"))
print(s.isLongPressedName("halllla", "hallaa"))
print(s.isLongPressedName("halo", "hola"))
print(s.isLongPressedName("saeed","ssaaedd"))
print(s.isLongPressedName("pyplrz",
"ppyypllr"))
print(s.isLongPressedName("alex", "alexxr"))