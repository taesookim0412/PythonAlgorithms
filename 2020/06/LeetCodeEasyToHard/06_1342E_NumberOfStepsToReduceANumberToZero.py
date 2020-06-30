#Runtime: 44 ms, faster than 11.28% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
#Memory Usage: 13.9 MB, less than 38.36% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ct = 0
        while num != 0:
            ct+=1
            if num == 1:
                num -=1
            elif num%2 == 0:
                num//=2
            elif num%2 != 0:
                num -= 1
        return ct