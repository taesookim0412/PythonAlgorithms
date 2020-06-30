#Runtime: 896 ms, faster than 5.09% of Python3 online submissions for Subrectangle Queries.
#Memory Usage: 15.6 MB, less than 60.00% of Python3 online submissions for Subrectangle Queries.

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        rect = self.rect
        for i in range(len(rect)):
            for j in range(len(rect[0])):
                if row1 <= i <= row2 and col1 <=j <= col2:
                    rect[i][j] = newValue
    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)