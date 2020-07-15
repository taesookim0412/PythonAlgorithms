from typing import List

#64.77% faster runtime
#35.76% less memory


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[j]) >= len(sol[i]):
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)


sol = Solution()
print(sol.largestDivisibleSubset([1,2,4,8]))
print(sol.largestDivisibleSubset([1,2,3]))
print(sol.largestDivisibleSubset([3,4,9]))
print(sol.largestDivisibleSubset([1,2,3,6]))
#4 8 240
print(sol.largestDivisibleSubset([4,8, 10, 240]))