#Runtime: 24 ms, faster than 92.02% of Python3 online submissions for Split a String in Balanced Strings.
#Memory Usage: 13.8 MB, less than 62.46% of Python3 online submissions for Split a String in Balanced Strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 0
        R = 0
        num = 0
        for i in range(len(s)):
            if s[i] == 'L':
                L+=1
            elif s[i] == 'R':
                R+=1
            if L==R:
                num+=1
                L=R=0
        return num
