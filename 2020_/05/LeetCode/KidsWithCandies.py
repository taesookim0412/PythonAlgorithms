# -*- coding: utf-8 -*-
from typing import List

#05-10-2020_
#Getting used to python again
#Switching projects due to incapabilities of my previous one
#This one has ml so here I am!

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= max
            print(candies[i])
        return candies

        
    
data = [2, 3, 5, 1, 3]
Solution().kidsWithCandies(data, 3)