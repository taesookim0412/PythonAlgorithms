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
# Complete the 'wifiZones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY zones as parameter.
#

#2/14
#Sorry but the description was not descriptive enough to put me in the shoes of Dijkstra himself.

#zones[[2,3],[1,5],[7,8],[1,2],[10,10]]
def wifiZones(zones):
    time_Deprived = 0
    lastMax = zones[0][1]
    for i in range(1, len(zones)):
        zone, prevZone = zones[i], zones[i-1]
        if zone[0] > lastMax:
            time_Deprived += 1
        lastMax = max(lastMax, zone[1])
    return time_Deprived

# def wifiZones(zones):
#     time_Deprived = 0
#     lastMax = zones[0][1]
#     for i in range(1, len(zones)):
#         zone, prevZone = zones[i], zones[i-1]
#         if zone[0] > lastMax:
#             time_Deprived = max(time_Deprived, zone[0] - lastMax)
#         lastMax = max(lastMax, zone[1])
#     return time_Deprived

    # Write your code here
if __name__ == '__main__':