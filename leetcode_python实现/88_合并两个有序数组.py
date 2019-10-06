from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n -1
        cur_1 = m - 1
        cur_2 = n - 1
        while cur >= 0:
            if cur_1 < 0:
                nums1[cur] = nums2[cur_2]
                cur_2 -= 1
            elif cur_2 < 0:
                nums1[cur] = nums1[cur_1]
                cur_1 -= 1
            elif nums1[cur_1] > nums2[cur_2]:
                nums1[cur] = nums1[cur_1]
                cur_1 -= 1
            else:
                nums1[cur] = nums2[cur_2]
                cur_2 -= 1
            cur -= 1


s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)



