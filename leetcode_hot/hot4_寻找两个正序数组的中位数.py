class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        if n > m:
            n, m = m, n
            nums1, nums2 = nums2, nums1
        odd = (n + m) % 2 == 1

        l, r = 0, n
        while l <= r:
            i = (l + r) // 2
            j = (n + m) // 2 - i
            
            if i > 0 and j < m and nums1[i-1] > nums2[j]:
                r = i - 1
            elif j > 0 and i < n and nums2[j-1] > nums1[i]:
                l = i + 1
            else:
                if odd:
                    if i == n:
                        return nums2[j]
                    elif j == m:
                        return nums1[i]
                    else:
                        return min(nums1[i], nums2[j])
                else:
                    if i == 0 and j == 0:
                        return nums1[0] if n > 0 else nums2[0]
                    a = nums1[i-1] if i > 0 else -1e8
                    b = nums2[j-1] if j > 0 else -1e8
                    c = nums1[i] if i < n else 1e8
                    d = nums2[j] if j < m else 1e8
                    return (max(a, b) + min(c, d)) / 2
        return 0
        
s = Solution()
nums1 = [1, 2]
nums2 = [3, 4]

print(s.findMedianSortedArrays(nums1, nums2))
