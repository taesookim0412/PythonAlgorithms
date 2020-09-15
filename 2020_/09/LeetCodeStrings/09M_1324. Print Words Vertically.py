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


# Input
# "TO BE OR NOT TO BE"
# Output
# ["TBONTB","OEROOE","T"]
# Expected
# ["TBONTB","OEROOE","   T"]

# Runtime: 36 ms, faster than 33.18% of Python3 online submissions for Print Words Vertically.
# Memory Usage: 13.8 MB, less than 61.22% of Python3 online submissions for Print Words Vertically.
def printVertically(self, s: str) -> List[str]:
    words = list(filter(None, s.split(' ')))
    longest_Len = len(max(words, key=len))
    res = [[' ' for _ in range(len(words))] for _ in range(longest_Len)]
    print(res)
    for i in range(longest_Len):
        for j in range(len(words)):
            res[i][j] = words[j][i] if len(words[j]) > i else ' '
    print(res)
    # just remove trailing spaces bro

    return [''.join(x).rstrip() for x in res]


print(printVertically(0, "HOW ARE YOU"))
print(printVertically(0,   "HOW ARE YOUU"))
print(printVertically(0,   "TO BE OR NOT TO BE"))