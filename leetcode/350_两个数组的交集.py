from typing import List
from collections import Counter
class Solution_1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d1 = {c: nums1.count(c) for c in set(nums1)}
        d2 = {c: nums2.count(c) for c in set(nums2)}
        for key, val in d1.items():
            if key in d2:
                res.extend([key]*min(d1[key], d2[key]))
        return res

class Solution_2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res
