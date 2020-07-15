from collections import Counter
from typing import List
import heapq

#Runtime: 108 ms, faster than 58.31% of Python3 online submissions for Top K Frequent Elements.
#Memory Usage: 18.3 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
#Priority Queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), counts.get)



print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([3, 2, 2, 1, 1, 1], 2))

print(Solution().topKFrequent([1, 2], 2))

