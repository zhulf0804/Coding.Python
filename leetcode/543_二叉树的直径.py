# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left + right > self.res:
                self.res = left + right
            return max(left, right) + 1
        helper(root)
        return self.res
