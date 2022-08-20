class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        res = [root.val]
        def core(root):
            if not root:
                return 0
            left = core(root.left)
            right = core(root.right)
            cur = root.val + max(left, 0) + max(right, 0)
            if cur > res[0]:
                res[0] = cur
            return max(0, max(left, right)) + root.val
        core(root)
        return res[0]
    