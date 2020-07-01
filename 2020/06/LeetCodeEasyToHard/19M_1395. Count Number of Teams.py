from typing import List

#lol its a high acceptance rating because no one submitted anything
#TODO: READ
#nope
# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         dp = [[0 for _ in range(len(rating))] for _ in range(len(rating))]
#         for i in range(len(rating)):
#             for j in range(len(rating)):
#                 dp[i][j] = abs(rating[j] - rating[i])
#         print(np.asmatrix(dp))
#
#
# import numpy as np
#nope
# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         ith = [0 for _ in range(len(rating)+1)]
#         jth= [0 for _ in range(len(rating)+2)]
#         kth = [0 for _ in range(len(rating)+3)]
#         for i in range(len(rating)):
#             ith[i+1] = ith[i] + rating[i]
#         for j in range(len(rating)):
#             jth[j+2] = jth[j+1] + rating[j]
#         for k in range(len(rating)):
#             kth[k+3] = kth[k+2] + rating[k]
#         print(ith)
#         print(jth)
#         print(kth)


s = Solution()
print(s.numTeams([2,5,3,4,1]))
print(s.numTeams([2,1,3]))

