import collections
import numpy as np
from typing import List

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.

#yeah dude that doesnt work if u tell us to do something in steps like that
#Repeat step 5 until you cannot pick more characters.
#"Repeat the steps from 1 to 6 until you pick all characters from s."
#but i thought u already picked all the characters
#dont walk me to through your terrible instructions
#its like getting navigation to the middle of a desert
#like u cant just slap that on at the last step
class Solution:
    def sortString(self, s: str) -> str:
        res = []
        s2 = list(sorted(set(s)))
        res += s2



        print(s2)

print(Solution().sortString("aaaabbbbcccc"))
