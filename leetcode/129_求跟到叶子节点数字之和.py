# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        def dfs(child_root, cur):
            if not child_root.left and not child_root.right:
                res[0] += cur * 10 + child_root.val
            if child_root.left:
                dfs(child_root.left, cur * 10 + child_root.val)
            if child_root.right:
                dfs(child_root.right, cur * 10 + child_root.val)
        dfs(root, 0)
        return res[0]