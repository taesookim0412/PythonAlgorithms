import collections
import heapq
from typing import List



#Runtime: 80 ms, faster than 81.65% of Python3 online submissions for Reconstruct Itinerary.
#Memory Usage: 14 MB, less than 84.32% of Python3 online submissions for Reconstruct Itinerary.

#heap solution
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketsMap = collections.defaultdict(dict)
        for i, a in enumerate(tickets):
            if not ticketsMap[a[0]]:
                ticketsMap[a[0]] = []
            heapq.heappush(ticketsMap[a[0]], a[1])
        dest = ["JFK"]
        visited = []
        while dest:
            while ticketsMap[dest[-1]]:
                dest += heapq.heappop(ticketsMap[dest[-1]]),
            visited += dest.pop(-1),
        return visited[::-1]


#17/80 doesn't visit every airport
#TODO: add double stack and route while loop
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketsMap = {}
        for i, a in enumerate(tickets):
            if a[0] not in ticketsMap:
                ticketsMap[a[0]] = [a[1]]
            else:
                heapq.heappush(ticketsMap[a[0]], a[1])
        print(ticketsMap)
        dest = ["JFK"]
        visited = []
        while len(dest) != 0:
            spot = heapq.heappop(dest)
            if spot in ticketsMap and len(ticketsMap[spot]) > 0:
                visited.append(spot)
                dest = ticketsMap[spot]


        return visited

#pochmann sol
#66.5
#51.42
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         targets = collections.defaultdict(list)
#         for a, b in sorted(tickets)[::-1]:
#             targets[a] += b,
#         route, stack = [], ['JFK']
#         while stack:
#             while targets[stack[-1]]:
#                 stack += targets[stack[-1]].pop(),
#             route += stack.pop(),
#         return route[::-1]

s = Solution()
print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print("Case Three:")
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))