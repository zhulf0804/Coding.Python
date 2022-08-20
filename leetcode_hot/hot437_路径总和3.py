# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        self.ans = 0
        def helper(root, cur):
            if not root:
                return
            cur = [item + root.val for item in cur]
            cur.append(root.val)
            c = 0
            for item in cur:
                if item == targetSum:
                    c += 1
            self.ans += c
            helper(root.left, cur)
            helper(root.right, cur)
        helper(root, [])
        return self.ans

