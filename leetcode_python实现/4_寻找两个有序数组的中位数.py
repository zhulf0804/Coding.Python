from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            #print(i, j, nums1, nums2)
            if i > 0 and j < n and nums1[i-1] > nums2[j]:
                imax = i - 1
            elif j > 0 and i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            else:
                if (m + n) % 2 == 1:
                    if i == 0:
                        return nums2[(m + n) // 2]
                    if j == 0:
                        return nums1[(m + n) // 2]
                    return max(nums1[i-1], nums2[j-1])


                if m == 0:
                    return (nums2[(m + n) // 2] + nums2[(m + n) // 2 - 1]) / 2

                if i == m:
                    right = nums2[j]
                    if j == 0:
                        left = nums1[i-1]
                    else:
                        left = max(nums1[i-1], nums2[j-1])
                elif i == 0:
                    left = nums2[j-1]
                    if j == n:
                        right = nums1[i]
                    else:
                        right = min(nums1[i], nums2[j])
                else:
                    left = max(nums1[i-1], nums2[j-1])
                    right = min(nums1[i], nums2[j])
                return (left + right) / 2

nums1 = []
nums2 = [2, 3]
obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))



