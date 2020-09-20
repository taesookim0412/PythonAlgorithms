import collections
import numpy as np
from typing import List



# Time complexity report:
# Iterate each companies,
# Iterate each hashed set,
# Determine in every entry in every subset
# This is N^2
#The problem with this solution stems from the following line:
#    if all(company in subset for company in companies):
#A simple hash lookup wouldve sealed the deal. However, finding a subset within every entry is killing runtime.
#The loop could've been resolve to finding the tuple in the set, instead there's an additional loop
#digging through every subset + digging through their entries.
#Alternative approaches:



# 53 / 55 test cases passed.
# Status: Time Limit Exceeded
# Submitted: 0 minutes ago
# Last executed input:
# [["vpxetwwrbrkuxnbspjds","efokucevmpehkvrtubqs","bssyzdscexlqlbsswufh","uhsteuhepwiyapfegyix","artcovcjypmkawwmvp
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        subsets = set()
        res = []
        for i, companies in enumerate(favoriteCompanies):
            for subset in subsets:
                if all(company in subset for company in companies):
                    res += i,
                    break
            subsets.update([tuple(companies)])
        subsets = set()
        for i, companies in zip(range(len(favoriteCompanies)-1, -1, -1), reversed(favoriteCompanies)):
            for subset in subsets:
                if all(company in subset for company in companies):
                    res += i,
                    break
            subsets.update([tuple(companies)])
        possRange = set([n for n in range(len(favoriteCompanies))])
        exclusive_res = possRange.symmetric_difference(res)
        return sorted(exclusive_res)

s = Solution()
#0, 1, 4
print(s.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
print(s.peopleIndexes([["amazon"],["amazon", "facebook"],["google","facebook"],["google"],["amazon"]]))