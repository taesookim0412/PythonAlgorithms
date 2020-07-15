#Holy Crap. 41 fairly easy algorithms, Math/Physics finals, and learned programming
#All in 12 days
#Actually have to review the algorithms now lmao.

#Runtime: 48 ms, faster than 66.61% of Python3 online submissions for Intersection of Two Arrays II.
#Memory Usage: 13.8 MB, less than 86.45% of Python3 online submissions for Intersection of Two Arrays II.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        data = {}
        res = []
        for i in range(len(nums1)):
            data[nums1[i]] = data.get(nums1[i], 0) + 1
        for i in range(len(nums2)):
            if nums2[i] in data and data[nums2[i]] > 0:
                res.append(nums2[i])
                data[nums2[i]] -=1
        return res