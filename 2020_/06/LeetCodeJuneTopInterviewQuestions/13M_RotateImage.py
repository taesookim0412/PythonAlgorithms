from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Reverse upside down
        matrix.reverse()
        m = len(matrix)
        n = len(matrix[0])

        #transpose for clockwise
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        """
        Do not return anything, modify matrix in-place instead.
        """

    #CCW:
    def rotateCCW(self, matrix: List[List[int]]) -> None:
        # Reverse L-R
        for i in range(len(matrix)): matrix[i].reverse()
        m = len(matrix)
        n = len(matrix[0])

        # transpose for CCW
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        """
        Do not return anything, modify matrix in-place instead.
        """
