# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        def helper(root):
            if not root:
                return 0, 0
            l1, l2 = helper(root.left)
            r1, r2 = helper(root.right)
            self.ans = max(self.ans, max(l1, l2) + max(r1, r2) + 1)
            return max(l1, l2) + 1, max(r1, r2) + 1
        helper(root)
        return self.ans - 1
