# -*- coding: utf-8 -*-

#05-18-2020_
#https://leetcode.com/problems/happy-number/
# Runtime: 36 ms, faster than 48.95% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Happy Number.
class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        completed = False
        sums = []
        print("NUM:", num)
        while completed==False:
            nl = []
            while (num > 0):
                nl.append(num%10)
                num //= 10
            sum = 0
            for a in nl: sum+=a*a
            if sum in sums: return False
            sums.append(sum)
            if sum==1: return True
            num = sum
        return False
        
    
    def __init__(self):
        print(self.isHappy(19))
Solution()