from typing import List
import math


#undebuggable
#redo tomorrow

class Solution:
    target = -1
    maxLower = 0
    minUpper = 0
    minIdx = 0
    maxIdx = 0

    #found the range of the rotatated array
    #however caught on that you can pass index to a merge traverse late
    #remake one tomorrow with the correct objective
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        if nums[0] == target: return 0
        self.target = target
        self.maxLower = nums[len(nums)-1]
        self.minUpper = nums[0]
        maxLowerClone = self.maxLower
        minUpperClone = self.minUpper
        #C1
        if (target > self.maxLower and target < self.minUpper): return -1
        #C2: Divide and conquer
        #Goal: find pivots (min -> max)
        self.totIdx = len(nums)-1
        self.divideAndConquer(nums, len(nums)-1, (len(nums)-1)//2)
        if not self.maxLower <= target <= self.minUpper: return -1
        if target == self.minIdx:
            return self.maxIdx
        elif target == self.maxIdx:
            return self.minIdx
        # min = self.maxLower
        # max = self.minUpper
        # print(min, max)
        #if in between
        # if target > min and target < max:
        #     if target < maxLowerClone:
        #         for i in range(len(nums), -1, -1):
        #             if nums[i] == target:
        #                 return len(nums)-1-i
        #     elif target > minUpperClone:
        #         for i in range(len(nums)):
        #             if nums[i] == target:
        #                 return i
        return self.targetIdx

    targetIdx = -1
    #pass-by-object-reference
    def divideAndConquer(self, nums, listIdx = 0, half = 0):
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]
            secondHalf = half
            if half == mid: secondHalf = 0

            self.divideAndConquer(L, mid)
            self.divideAndConquer(R, half + secondHalf)
            #print(listIdx)

            #maxLower turns to Min
            #minUpper turns to Max
            if len(L) ==1 and len(R) == 1:
                print(listIdx)
                #print(L, R)
                if L[0] < self.maxLower or R[0] < self.maxLower:
                    self.maxLower = min(L[0], R[0], self.maxLower)
                    self.minIdx = (listIdx -1) if self.maxLower == L[0] else (listIdx + 1) if self.maxLower == R[0] else self.minIdx
                    if L[0] == self.target: self.targetIdx = listIdx - 1
                    elif R[0] == self.target: self.targetIdx = listIdx
                if L[0] > self.minUpper or R[0] > self.minUpper:
                    self.minUpper = max(L[0], R[0], self.minUpper)
                    self.maxIdx = (listIdx - 1) if self.minIdx == L[0] else (listIdx + 1) if self.minIdx == R[0] else self.maxIdx
                    if L[0] == self.target: self.targetIdx = listIdx - 1
                    elif R[0] == self.target: self.targetIdx = listIdx
            elif len(L) ==1 or len(R) == 1:
                side = R if len(L) != 1 else L
                offset = -1
                if side == R:
                    offset = 1
                print(side)
                for i in range(0, len(side)):
                    offset += i
                    if side[i] < self.maxLower:
                        self.maxLower = side[i]
                        self.minIdx = listIdx + offset
                    if side[i] > self.minUpper:
                        self.minUpper = side[i]
                        self.maxIdx = listIdx + offset
                    if side[i] == self.target: self.targetIdx = listIdx + offset








    def __init__(self):
        print(self.search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
        #-1
        #print(self.search([3, 4, 5, 6, 1, 2], 0) == -1)
        #2
        #print(self.search([3, 4, 5, 7, 1, 2], 5))
        #4
        print(self.search([4, 5, 6, 7, 0, 1, 2], 0))
        #1
        #print(self.search([1, 3], 3))




Solution()