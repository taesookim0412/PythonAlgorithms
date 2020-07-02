#Runtime: 40 ms, faster than 62.06% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Memory Usage: 13.9 MB, less than 52.30% of Python3 online submissions for Number of Students Doing Homework at a Given Time.

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num = 0
        for i, a in enumerate(startTime):
            b = endTime[i]
            if a <= queryTime <= b:
               num += 1
        return num