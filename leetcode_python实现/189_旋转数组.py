class Solution_1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        left = nums[:-k]
        right = nums[-k:]
        nums[0:k] = right
        nums[k:] = left

class Solution_2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:-k]

class Solution_3(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        start = 0
        n = len(nums)
        count = 0
        while start < n and count < n:
            next = (start + k) % n
            tmp = nums[start]
            while next != start:
                next_val = nums[next]
                nums[next] = tmp
                next = (next + k) % n
                tmp = next_val
                count += 1
            nums[next] = tmp
            count += 1
            start += 1
