from typing import List

#05/11/2020_
#Runtime: 44 ms, faster than 91.10% of Python3 online submissions for Move Zeroes.
#Memory Usage: 15.2 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
#https://leetcode.com/problems/move-zeroes/submissions/

def moveZeroes(nums: List[int]) -> None:
    zeros = 0
    for i in range(0, len(nums)):
        if nums[i] == 0: 
            zeros+=1
            continue
        nums[(i - zeros)] = nums[i]
        if zeros > 0: nums[i] = 0
        print(zeros)
    print(nums)
        
    
#1, 3, 12, 0, 0
moveZeroes([0, 1, 0, 3, 12])
moveZeroes([0, 0, 1])
moveZeroes([0, 0, 0, 1])
moveZeroes([0, 1, 0])