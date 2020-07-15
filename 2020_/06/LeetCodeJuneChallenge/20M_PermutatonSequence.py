import itertools

#Runtime: 2116 ms, faster than 11.80% of Python3 online submissions for Permutation Sequence.
#Memory Usage: 57.2 MB, less than 5.04% of Python3 online submissions for Permutation Sequence.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perms = list(itertools.permutations([i for i in range(1, n+1)]))
        return ''.join(str(i) for i in perms[k-1])



#ok but its the heap algorithm how is it the wrong solution
class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        self.perms = []
        self.nums = [i for i in range(1, n+1)]
        self.heapPermutations(n)
        print(self.perms)
        return (''.join((str(i) for i in self.perms[k-1])))


    def heapPermutations(self, n):
        nums = self.nums
        if n == 1:
            self.perms.append(list(nums))
        for i in range(n):
            self.heapPermutations(n-1)
            if n & 1:
                nums[0], nums[n-1] = nums[n-1], nums[0]
            else:
                nums[i], nums[n-1] = nums[n-1], nums[i]

s = Solution()
print(s.getPermutation(3, 3))