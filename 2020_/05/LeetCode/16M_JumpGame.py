from typing import List
#Runtime: 108 ms, faster than 22.16% of Python3 online submissions for Jump Game.
#Memory Usage: 16.2 MB, less than 7.14% of Python3 online submissions for Jump Game.

class Solution:
    #original solution review:
    #DP sums array
    #sums[i+1] = max(num, sums[i]) with phi at i=0
    #make conds for 0 steps
    #decrement by a step
    #O(n) runtime, O(n) extra space array for sums.
    def canJumpOrig(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        sums = [0] * (len(nums) + 1)
        for i in range(0, len(nums)-1):
            sums[i+1] = max(sums[i], nums[i])
            #print(sums)
            if sums[i+1]<=0 and nums[i] == 0: return False
            if (nums[i] + i) >= len(nums)-1 and nums[i] != 0: return True
            sums[i+1] -= 1
        return False

#Runtime: 96 ms, faster than 43.27% of Python3 online submissions for Jump Game.
#Memory Usage: 16.1 MB, less than 7.14% of Python3 online submissions for Jump Game.
#Optimized to mutate the original list
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        if nums[0] >= len(nums)-1: return True
        if (nums[0] == 0): return False
        for i in range(1, len(nums)-1, 1):
            if i == 1: nums[0] -=1
            nums[i] = max(nums[i-1], nums[i])
            if nums[i]<=0 and nums[i] == 0: return False
            if (nums[i] + i) >= len(nums)-1 and nums[i] != 0: return True
            nums[i] -= 1
        return False
    def __init__(self):
        #T
        print(self.canJump([2, 3, 1, 1, 4]) == True)
        #F
        print(self.canJump([3, 2, 1, 0, 4]) == False)
        #T
        print(self.canJump([0]) == True)
        #T
        print(self.canJump([1, 2]) == True)
        #F
        print(self.canJump([0, 2, 3]) == False)
        #F
        print(self.canJump([1, 1, 0, 1]) == False)
        #F
        print(self.canJump([1, 0, 1, 0]) == False)
        #T
        print(self.canJump([2, 0, 2, 0, 1]) == True)
        #F
        print(self.canJump([5,4,0,2,0,1,0,1,0]) == False)


    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums)==1: return True
    #     dp = [0] * (len(nums) + 1)
    #     for i in range(0, len(nums)-1):
    #         dp[i+1] = (len(nums)-1) - (dp[i] + nums[i])
    #         print(dp)
    #         #ec
    #         if nums[i] != 0:
    #             if dp[i+1] <= 0: return True
    #     print(dp)
    #     return False


Solution()