class Solution:
    def findKthLargest(self, nums, k):
        def partition(nums, l, r):
            pivot = nums[r]
            i, j = l, r - 1
            while i <= j:
                if nums[i] <= pivot:
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def select(nums, k, l, r):
            pivot_idx= partition(nums, l, r)
            if pivot_idx == k:
                return nums[k]
            elif pivot_idx < k:
                return select(nums, k, pivot_idx + 1, r)
            else:
                return select(nums, k, l, pivot_idx - 1)

        return select(nums, len(nums) - k, 0, len(nums)-1)        
        