from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []

        def dfs(child_root, cur):
            if not child_root.left and not child_root.right:
                res.append(cur + str(child_root.val))
                return
            if child_root.left:
                dfs(child_root.left, cur + str(child_root.val) + "->")
            if child_root.right:
                dfs(child_root.right, cur + str(child_root.val) + "->")
        dfs(root, "")
        return res