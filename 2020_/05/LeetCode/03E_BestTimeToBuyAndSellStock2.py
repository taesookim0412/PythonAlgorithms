#AR: 55.9%
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#05-15-2020_
#great problem learned a lot didn't spend over an hour trying to dynamically program it
#lots of life lessons if the price is higher the next day then sell it
#also im improving my one liners
#Runtime: 60 ms, faster than 81.77% of Python3 online submissions for Best Time to Buy and Sell Stock II.
#Memory Usage: 15.1 MB, less than 7.32% of Python3 online submissions for Best Time to Buy and Sell Stock II.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
                    
        
    def __init__(self):
        print(self.maxProfit([1, 2, 5, 3, 5]))
        print(self.maxProfit([7,1,5,3,6,4]))
        
Solution()