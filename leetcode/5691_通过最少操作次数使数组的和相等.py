from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        summ1, summ2 = sum(nums1), sum(nums2)
        len1, len2 = len(nums1), len(nums2)
        if 6 * len2 < len1 or 6 * len1 < len2:
            return -1
        if summ1 == summ2:
            return 0
        if summ1 < summ2:
            nums1, nums2 = nums2, nums1
            summ1, summ2 = summ2, summ1
            len1, len2 = len2, len1
        i, j = len1 - 1, 0
        ans = 0
        diff = summ1 - summ2
        while diff > 0:
            ans += 1
            if i < 0 and j < len2:
                cur = 6 - nums2[j]
                diff -= cur
                j += 1
            elif i >= 0 and j >= len2:
                cur = nums1[i] - 1
                diff -= cur
                i -= 1
            elif i >= 0 and j < len2:
                if nums1[i] - 1 > 6 - nums2[j]:
                    cur = nums1[i] - 1
                    diff -= cur
                    i -= 1
                else:
                    cur = 6 - nums2[j]
                    diff -= cur
                    j += 1
        return ans
