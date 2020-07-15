import collections
import numpy as np
from typing import List

#"abcd aabc bd"
#"aaa aa"
#[3,2]
#3 strings with frequency smaller than B_0,
#2 strings with frequency smaller than B_1
#Smaller when the frequency of occurnece is less than freq in larger string

class Solution:
    def compareStrings(self, aL:List[str], bL:List[str]):
        res = [0 for _ in range(len(bL))]
        aL.sort()
        for i in range(len(bL)):
            a = bL[i]
            l = 0
            r = len(a)-1
            while l < r:
                mid = l + (r-l)//2
                #I dont think this will work anymore, it could use a two pointer approach though.
            res[i] = l
        return res


#O(N^2) Runtime
class Solution2:
    def compareStrings(self, aL:List[str], bL:List[str]):
        res = [0 for _ in range(len(bL))]
        for i in range(len(bL)):
            b = bL[i]
            for j in aL:
                res[i] += self.countFrequencies(b, j)
        return res
    #a = b[i], j = a
    def countFrequencies(self, b, j):
        if b[0] < j[0]:
            return 1
        elif b[0] > j[0]:
            return 0
        char = b[0]
        bCt = b.count(char)
        jCt = j.count(char)
        print(bCt, jCt)
        if bCt > jCt:
            return 1
        elif bCt < jCt:
            return 0
        if b > j:
            return 1
        return 0





s = Solution2()
print(s.compareStrings(["abcd","aabc","bd"],["aaa","aa"]))