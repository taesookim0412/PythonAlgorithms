import collections
import numpy as np
from typing import List
#!/bin/python3

import math
import os
import random
import re
import sys


#100%

#
# Complete the 'getMatches' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
# abc123 liked xyz
# xyz liked abc123
import collections
# xyz liked by abc123
# dict[xyz]: abc123 exists thus append [p1, p2]
def getMatches(events):
    likes = collections.defaultdict(list)
    res = []
    for pair in events:
        p1 = pair[0]
        p2 = pair[1]
        if likes[p1] and p2 in likes[p1]:
            res.append([p2, p1])
        else:
            likes[p2] += p1,
    return res