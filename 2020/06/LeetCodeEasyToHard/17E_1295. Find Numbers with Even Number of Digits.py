#Runtime: 60 ms, faster than 35.52% of Python3 online submissions for Find Numbers with Even Number of Digits.
#Memory Usage: 13.9 MB, less than 57.04% of Python3 online submissions for Find Numbers with Even Number of Digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for x in nums:
            if len(str(x))%2 ==0:
                evens +=1
        return evens