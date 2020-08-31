#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalFrequency' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING oldPassword as parameter.
#
import collections


#???????
#2/14

def equalFrequency(oldPassword):
    dp = [len(list(val)) for key, val in itertools.groupby(oldPassword)]
    totalOnes = []
    ones = 0
    for i in range(1, len(dp)):
        dp[i] = max(min(dp[i], dp[i - 1]) + dp[i], dp[i - 1])
        if dp[i] != dp[i - 1]:
            ones += 1
        else:
            totalOnes += ones,
            ones = 0
    print(dp)
    return max(dp + totalOnes)


# abbccd
# abbbccd


# retrieve longest substring with highest frequencies.
# groupby
# aaaabbbcb
# 4,3,1,1
# dp
# 4, min(4, 3) + 3 = 6, max(min(i-1, i) + i), dp[i-1])
# 4, 6, 6, 6
# min i-1
# 33 = 6

# abcde
# 1,1,1,1,1
# 5
# accbbe
# 1,2,2,1
# 4
import itertools

# def equalFrequency(oldPassword):
#     dp = [len(list(val)) for key, val in itertools.groupby(oldPassword)]
#     for i in range(1, len(dp)):
#         dp[i] = max(min(dp[i], dp[i-1])+ dp[i], dp[i-1])
#     return dp[-1]


# retrieve counter
# sort by counter occurences
# retrieve longest running string len
# def equalFrequency(oldPassword):
#     # Write your code here
#     chCt = collections.Counter(oldPassword)
#     ranges = collections.defaultdict(int)
#     #lowest to highest order
#     for key, val in chCt.items():
#         ranges[val] += val
#     return max(ranges.values())