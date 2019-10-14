# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.summ = 0
        def helper(root):
            if not root:
                return
            if root.left:
                if not root.left.left and not root.left.right:
                    self.summ += root.left.val
                helper(root.left)
            helper(root.right)
        helper(root)
        return self.summ