from typing import List

#Don't understand the que
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 1: return matrix[0][0]
        i = k // n
        j = k % n -1
        return matrix[i][j]

sol = Solution()
print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))