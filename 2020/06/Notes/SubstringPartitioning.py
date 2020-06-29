from typing import List

#TODO: Subset of backtracking

def receivePartitions(s, idx):
    res = []
    for i in range(1, len(s)+1):
        data = [s[:i]]
        for x in receivePartitions(s[i:], i):
            res.append(x+data)
            print(f"x: {x}")
            print(res)
    if not res:
        return [[]]
    return res

#FIRST:
#Deepest subproblem [[i==n-1:n]:] + [[


print(receivePartitions("hello",0))