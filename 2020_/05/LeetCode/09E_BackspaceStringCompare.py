import itertools

#05-19-2020_
#Runtime: 56 ms, faster than 5.44% of Python3 online submissions for Backspace String Compare.
#Memory Usage: 14 MB, less than 8.00% of Python3 online submissions for Backspace String Compare.
#https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str1 = list(S)
        str2 = list(T)
        self.processBackspace(str1)
        self.processBackspace(str2)
        S = ''.join(str1)
        T = ''.join(str2)
        print(str1)
        print(str2)
        print(S, T)
        str3 = list(str2)
        return S == T

    def processBackspace(self, str1):
        idx = len(str1)
        htags = 0
        while idx > 0:
            idx-= 1
            if str1[idx] == '#':
                htags+=1
                del str1[idx]
                continue
            if htags > 0:
                del str1[idx]
                htags -= 1

#itertools ver:
#Runtime: 32 ms, faster than 43.12% of Python3 online submissions for Backspace String Compare.
#Memory Usage: 13.7 MB, less than 8.00% of Python3 online submissions for Backspace String Compare.

    def backSpaceCompareConstantSpace(self, S, T):
        def F(s):
            skip = 0
            for x in reversed(s):
                if x == '#':
                    skip +=1
                elif skip:
                    skip -=1
                else:
                    yield x
        return all(x==y for x, y in itertools.zip_longest(F(S), (F(T))))


    def __init__(self):
        print(self.backspaceCompare("ab#c", "ad#c"))
        print(self.backspaceCompare("ab##", "c#d#"))
        print(self.backspaceCompare("xywrrmp","xywrrmu#p"))
        print(self.backSpaceCompareConstantSpace("ab#c", "ad#c"))
        print(self.backSpaceCompareConstantSpace("ab##", "c#d#"))
        print(self.backSpaceCompareConstantSpace("xywrrmp", "xywrrmu#p"))

Solution()
