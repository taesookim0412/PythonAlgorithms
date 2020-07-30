import collections
from collections import Counter
import numpy as np
from typing import List


#Sort a list of every odd element
#Sort a list of every even element
#Create a set of the combination
#Return its length

#Runtime: 56 ms, faster than 50.93% of Python3 online submissions for Groups of Special-Equivalent Strings.
#Memory Usage: 14.1 MB, less than 27.27% of Python3 online submissions for Groups of Special-Equivalent Strings.

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for strX in A:
            odd_Elements = sorted(strX[x] for x in range(len(strX)) if x & 1)
            even_Elements = sorted(strX[x] for x in range(len(strX)) if not x & 1)
            combination = odd_Elements + even_Elements
            res.update([tuple(combination)])
        return len(res)
s = Solution()
print(s.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))









#Count the number of groups:
#Pop from the list
#Return len of the group stack



#Runtime: 4864 ms, faster than 5.32% of Python3 online submissions for Groups of Special-Equivalent Strings.
#Memory Usage: 14 MB, less than 54.55% of Python3 online submissions for Groups of Special-Equivalent Strings.

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = []
        while len(A) > 0:
            comparisons = []
            strI = A.pop()
            res.append([strI])
            oddACts = Counter([strI[x] for x in range(len(strI)) if x & 1 == 1])
            evenACts = Counter([strI[x] for x in range(len(strI)) if x & 1 == 0])
            while len(A) > 0:
                B = A.pop()
                oddBCts = Counter([B[x] for x in range(len(strI)) if x & 1 == 1])
                evenBCts = Counter([B[x] for x in range(len(strI)) if x & 1 == 0])
                if oddACts == oddBCts and evenACts == evenBCts:
                    res[-1] += B
                else:
                    comparisons.append(B)
            if len(A) == 0:
                A = comparisons
        return len(res)












#Count all the odds occurences
#Count all even occurences
#Compare (n^2)

class Solution2:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        maxCt = 0
        for i in range(len(A)):
            strI = A[i]
            oddCts = Counter([strI[x] for x in range(len(strI)) if x&1 == 1])
            evenCts = Counter([strI[x] for x in range(len(strI)) if x&1 == 0])
            specialCt = 0
            for j in range(len(A)):
                strJ = A[j]
                oddJCts = Counter([strJ[x] for x in range(len(strJ)) if x&1 == 1])
                evenJCts = Counter([strJ[x] for x in range(len(strJ)) if x&1 == 0])
                specialCt += 1 if oddCts == oddJCts and evenCts == evenJCts else 0
            maxCt = max(maxCt, specialCt)
        return maxCt

s = Solution()
print(s.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
print(s.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))