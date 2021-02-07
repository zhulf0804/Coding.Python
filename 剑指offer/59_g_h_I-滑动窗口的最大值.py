'''
双指针list, 始终维持递减序列, 存储索引
idxl始终指向最大值, idxr指向list的最右端元素
逐次遍历num : nums, 考勤把其索引插入list
1. 若此时元素长度大于k, 则idxl右移一位，继续2
2. 从idxr逆向遍历list, 找到最后一个 <= num 的元素的位置，将num的索引插入list[idxr]
3. 若i + 1 >= k, 即窗口宽度大于等于k，需要计算最大值
'''

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        mmax, idxl, idxr = [0] * n, 0, 0
        res = []
        if k == 1:
            res.append(nums[0])
        for i in range(1, n):
            if i - mmax[idxl] + 1 > k:
                idxl += 1
            while idxr >= idxl and nums[mmax[idxr]] <= nums[i]:
                idxr -= 1
            idxr += 1
            mmax[idxr] = i
            if i >= k - 1:
                res.append(nums[mmax[idxl]])
        return res

nums = [1,3,1,2,0,5]
k = 3
a = Solution()
print(a.maxSlidingWindow(nums, k))