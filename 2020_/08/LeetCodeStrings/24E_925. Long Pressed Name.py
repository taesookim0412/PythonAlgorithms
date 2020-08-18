import collections
import numpy as np
from typing import List


#Wrong
#GroupBy Solution required

#12011
#waada
#130011
#waaada

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
        nI, tI = 0, 0
        print(namedNums, typedNums)
        for i in range(len(typed)):
            if typedNums[tI] == 0:
                tI -=1
            if typedNums[nI] == 0 :
                nI -= 1
            if typedNums[tI] < namedNums[nI] or typed[tI] != name[nI]:
                return False
            nI +=1
            tI += 1
        return True

s = Solution()
print(s.isLongPressedName("wada", "waada"))
print(s.isLongPressedName("halllla", "hallaa"))
print(s.isLongPressedName("halo", "hola"))
print(s.isLongPressedName("saeed","ssaaedd"))