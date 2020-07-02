from typing import List

#Runtime: 100 ms, faster than 13.00% of Python3 online submissions for Minimum Time Visiting All Points.
#Memory Usage: 13.9 MB, less than 31.38% of Python3 online submissions for Minimum Time Visiting All Points.
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalDist = 0
        for i in range(1, len(points)):
            xoff = abs(points[i][0] - points[i-1][0])
            yoff = abs(points[i][1] - points[i-1][1])
            totalDist += max(xoff, yoff)
        return totalDist


























#
#In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
#so you can only move perfectly horizontally in one second because yeah
#graphs
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #wtf
        totalDist = 0
        for i in range(1,len(points)):
            xoff = points[i][0] - points[i-1][0]
            yoff = points[i][1] - points[i-1][1]
            totalDist += (xoff **2 + yoff **2)**(1/2)
        return totalDist

