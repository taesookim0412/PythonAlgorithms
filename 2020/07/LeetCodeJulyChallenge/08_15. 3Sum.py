import collections
import numpy as np
from typing import List




#List then iterating the list. Hashing for constant lookup.


#Alternative answer: Sort, Add only the positive numbers
#-> Basically the opposite of my first approach. Hash in O(n) and append triples in O(n^2).
#(Append in N^2 with outer for loop iterating negatives.)

#Still, an approach without sort is pretty unique.
#(I've actually gotten TLE's based mostly on the fact that I've used sort).

#Runtime: 472 ms, faster than 97.40% of Python3 online submissions for 3Sum.
#Memory Usage: 17.6 MB, less than 26.98% of Python3 online submissions for 3Sum.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos = []
        zeros = []
        negatives = []
        res = set()
        for num in nums:
            if num > 0:
                pos += num,
            elif num == 0:
                zeros += num,
            elif num < 0:
                negatives += num,
        if len(zeros) > 0:
            for i in pos:
                if (-i) in negatives:
                    res.add(tuple(sorted([-i, 0, i])))
        P, N = set(pos), set(negatives)
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = -(pos[i]+pos[j])
                if target in N:
                    res.add(tuple(sorted([target, pos[i], pos[j]])))
        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                target = -(negatives[i]+negatives[j])
                if target in P:
                    res.add(tuple(sorted([negatives[i], negatives[j], target])))
        if len(zeros) >= 3:
            res.add((0,0,0))
        return res







#dang i tried this a year ago, got TLE
#tried this again, still got TLE.
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = collections.defaultdict(list)
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                summation = nums[i] + nums[j]
                sums[summation] += i, j,
        for i in range(len(nums)):
            sumList = sums[-nums[i]]
            for j in range(0,len(sumList), 2):
                if i != sumList[j] and i != sumList[j+1] and sumList[j] != sumList[j+1]:
                    res.update([tuple(sorted([nums[i], nums[sumList[j]], nums[sumList[j+1]]]))])
        return list(res) if len(res) > 0 else []


        # for i in range(nums):
        #     diff = -nums[i]
        #     if sums[diff]:
        #         res.append([i, *sums[diff]])
        #     sums[diff] +=
        print(sums)
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,0]))