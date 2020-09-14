import collections
import numpy as np
from typing import List

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically.
#  "HAY"
#  "ORO"
#  "WEU"

#["HAY" -> First letter of each word]

# Split the words by delimiter ' ',
# find the len of the longest word
# fix list size of len
# inverted for loop


# 2/32
# Input
# "TO BE OR NOT TO BE"
# Output
# ["TBONTB","OEROOE","T"]
# Expected
# ["TBONTB","OEROOE","   T"]
def printVertically(self, s: str) -> List[str]:
    words = list(filter(None, s.split(' ')))
    longest_Len = len(max(words, key=len))
    res = ['' for _ in range(longest_Len)]
    for i in range(longest_Len):
        for j in range(len(words)):
            res[i] += words[j][i] if len(words[j]) > i else ''
    return res


printVertically(0, "HOW ARE YOU")
printVertically(0, "HOW ARE YOUU")