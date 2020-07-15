# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
#Runtime: 132 ms, faster than 5.42% of Python3 online submissions for Flatten Nested List Iterator.
#Memory Usage: 17.8 MB, less than 5.21% of Python3 online submissions for Flatten Nested List Iterator.
#stack iterator
class NestedIterator:
    def __init__(self, nestedList: [int]):
        self.stack = nestedList[::-1]
        print(self.stack)
    def next(self) -> int:
        return self.stack.pop().getInteger()
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]

# class NestedIterator:
#     def __init__(self, nestedList: [int]):
#         self.stack = [[nestedList, 0]]
#     def next(self) -> int:
#         self.hasNext()
#         nestedList, i = self.stack[-1]
#         self.stack[-1][1] += 1
#         return nestedList[i].getInteger()
#
#
#     def hasNext(self) -> bool:
#         s = self.stack
#         while s:
#             nestedList, i = s[-1]
#             if i == len(nestedList):
#                 s.pop()
#             else:
#                 x = nestedList[i]
#                 if x.isInteger():
#                     return True
#                 s[-1][1] += 1
#                 s.append([x.getList(), 0])
#             print(s)
#         return False

ni = NestedIterator([2, 3, 4, 2])
ni.hasNext()



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())