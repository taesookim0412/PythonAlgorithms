import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 83.35% of Python3 online submissions for Buddy Strings.
#Memory Usage: 13.9 MB, less than 63.49% of Python3 online submissions for Buddy Strings.


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        incorrect = None
        aCtr = collections.defaultdict(int)
        bCtr = collections.defaultdict(int)
        Alst = list(A)
        for i, (a, b) in enumerate(zip(A, B)):
            if a != b:
                if incorrect is None:
                    incorrect = i
                else:
                    Alst[incorrect], Alst[i] = Alst[i], Alst[incorrect]
                    return True if ''.join(Alst) == B else False
            aCtr[a] += 1
            bCtr[b] += 1
        # now determine if there are more then two of the same characters in each counter
        # The result is only true if the exclusion of those characters produce equal strings.
        for a, b in zip(sorted(aCtr.items(), key=lambda pair: pair[1]), sorted(bCtr.items(), key=lambda pair: pair[1])):
            if a[1] >= 2 and b[1] >= 2:
                return True if aCtr == bCtr else False
        return False


s = Solution()
print(s.buddyStrings("ab","ba"))
print(s.buddyStrings("aa","aa"))
print(s.buddyStrings("aaaaaaabc","aaaaaaacb"))
print(s.buddyStrings("","aa"))
print(s.buddyStrings("ab","ab"))
print(s.buddyStrings("",""))
print(s.buddyStrings("abac","abad"))



