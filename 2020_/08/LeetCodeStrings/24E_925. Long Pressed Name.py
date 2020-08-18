import collections
import numpy as np
from typing import List


#GroupBy Solution would be nice

#12011
#waada
#130011
#waaada

# Runtime: 60 ms, faster than 10.28% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 14 MB, less than 16.34% of Python3 online submissions for Long Pressed Name.

class Solution:
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
print(s.isLongPressedName("yomata", "youmata"))
print(s.isLongPressedName("teelee", "tteelee"))



print(s.isLongPressedName("halllla", "hallaa"))
print(s.isLongPressedName("halo", "hola"))
print(s.isLongPressedName("saeed","ssaaedd"))
print(s.isLongPressedName("pyplrz",
"ppyypllr"))