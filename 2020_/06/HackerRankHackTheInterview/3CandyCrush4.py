#AR: 71.16%
#30/30
#Medium

#CP is a lot different from LC, you can utilize extra memory..

def getMaxScore2(jewels):
    stack = []
    idx = 0
    ct = 0
    while idx < len(jewels):
        if len(stack)>0 and stack[-1]==jewels[idx]:
            stack.pop(-1)
            idx+=1
            ct+=1
        else:
            stack.append(jewels[idx])
            idx+=1
    return ct


























def getMaxScore(jewels):
    stack = []
    idx = 0
    ct = 0
    while idx < len(jewels):
        if len(stack) > 0 and stack[-1]==jewels[idx]:
            ct+=1
            stack.pop(-1)
        else:
            stack.append(jewels[idx])
        idx+=1
    return ct









print(getMaxScore("abcddcbd"))