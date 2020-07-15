# push(int)
# pop()
# top()
# getMin() - constant time
#
#
#
#
#
#
#
#
#
# 05-23-2020_
# Runtime: 68 ms, faster than 46.84% of Python3 online submissions for Min Stack.
# Memory Usage: 17.5 MB, less than 5.36% of Python3 online submissions for Min Stack.
# https://leetcode.com/problems/min-stack
#
# Doing things the hard way

class MinStack:
    stack = []
    minElemIdx = None

    def __init__(self):
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)
        if self.minElemIdx is None:
            self.minElemIdx = 0
        elif self.stack[len(self.stack) - 1] < self.stack[self.minElemIdx]:
            self.minElemIdx = len(self.stack) - 1

    def pop(self):
        del self.stack[len(self.stack) - 1]
        if self.minElemIdx == len(self.stack):
            if len(self.stack) == 0: return
            self.minElemIdx = self.stack.index(min(self.stack))
            # self.minElemIdx = min(range(len(self.stack)), key=self.stack.__getitem__)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stack[self.minElemIdx]
