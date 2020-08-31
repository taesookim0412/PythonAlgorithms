import collections
import numpy as np
from typing import List
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findPalindrome' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER q
#  3. INTEGER_ARRAY pos
#  4. CHARACTER_ARRAY ch
#

#2/14

def findPalindrome(s, q, pos, ch):
    # Write your code here
    res = []
    s_List = list(s)
    for idx, c in zip(pos, ch):
        s_List[idx] = c
        prev_Ct = len(res)
        for i in range(2, len(s_List)):
            if s_List[i] == s_List[i-2] or s_List[i] == s_List[i-1]:
                res.append("Yes")
                break
        if len(res) == prev_Ct:
            res.append("No")
    return res
