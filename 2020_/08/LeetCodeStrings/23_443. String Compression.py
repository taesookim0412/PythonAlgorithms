import collections
import numpy as np
from typing import List


#Wrong

#In place custom counter w/o 1 entries only char
#cccd
#c3d1

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         ct = 1
#         write = 1
#         for read in range(1, len(chars)):
#             if chars[read] != chars[read-1]:
#                 chars[write] = ct
#                 ct = 0
#                 write = write + 1
#             if read >= write:
#                 chars[write] = chars[read]
#                 write += 1
#             print(read, write)
#             ct += 1
#             read += 1
#         return chars







#
#
#
# class Solution2:
#     def compress(self, chars: List[str]) -> int:
#         ct = 0
#         trueIndex = 1
#         for i in range(1, len(chars)):
#             ct += 1
#             if chars[i] != chars[i-1] or i == len(chars)-1:
#                 if ct > 1:
#                     chars[trueIndex] = ct
#                     trueIndex += 2
#                 else:
#                     trueIndex += 1
#                 ct = 1
#                 #read, write, count pointer
#         print(chars)

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         def insert(pair, chars2):
#             chars.append(pair[0])
#             chars.append(str(pair[1]))
#         chars2 =  [insert(pair, chars2) if pair[1] > 1 else pair[0] for pair in collections.Counter(chars).items()]
#         print(chars2)


s = Solution()
print(s.compress(['c','c','c','d']))
print(s.compress(["a","a","b","b","c","c","c",'d']))
#print(s.compress(['a','b','c','d','d']))