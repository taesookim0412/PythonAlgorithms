import collections
import numpy as np
from typing import List

#Great questions from terribly constructed data structures
#Runtime: 404 ms, faster than 5.03% of Python3 online submissions for Employee Importance.
#Memory Usage: 14.9 MB, less than 51.87% of Python3 online submissions for Employee Importance.

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = 0
        subordinatesGlobal = set()

        def dfs(subordinates):
            nonlocal importance;
            for employee in employees:
                if employee.id in subordinates:
                    importance += employee.importance
                    if employee.subordinates:
                        dfs(set(employee.subordinates))

        for employee in employees:
            if employee.id == id:
                importance += employee.importance
                subordinatesGlobal.update(employee.subordinates)
        dfs(subordinatesGlobal)
        return importance