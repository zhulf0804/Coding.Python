class Solution:
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        flag = False
        # 查找相遇节点
        while slow != fast and flag:
            flag = True
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # 查找入环节点
        cur = 0
        while cur != slow:
            cur = nums[cur]
            slow = nums[slow]
        return cur
        