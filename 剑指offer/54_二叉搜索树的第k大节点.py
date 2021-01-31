from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = self.inorder(root)
        n = len(res)
        return res[n-k]