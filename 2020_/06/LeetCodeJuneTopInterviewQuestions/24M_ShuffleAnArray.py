#OMG I "flashed" my first medium problem.
#Runtime: 332 ms, faster than 64.72% of Python3 online submissions for Shuffle an Array.
#Memory Usage: 19 MB, less than 69.20% of Python3 online submissions for Shuffle an Array.
#Fisher-yates shuffle.

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums
        for i in range(len(nums)):
            rand = random.randrange(i, len(nums))
            nums[rand], nums[i] = nums[i], nums[rand]
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()