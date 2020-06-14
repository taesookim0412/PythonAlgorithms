import collections
import heapq
from typing import List

#Runtime: 120 ms, faster than 41.75% of Python3 online submissions for Cheapest Flights Within K Stops.
#Memory Usage: 19.3 MB, less than 29.21% of Python3 online submissions for Cheapest Flights Within K Stops.

#Dijkstra's Algorithm
class Solution:
    #[src, dist, cost]
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = collections.defaultdict(dict)
        for a, b, c in flights:
            f[a][b] = c
        heap = [(0, src, K+1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p+f[i][j], j, k-1))
        return -1

s = Solution()
print(s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))