# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root):
        if not root:
            return 0
        hl, hr = self.helper(root.left), self.helper(root.right)
        h = 1 + max(abs(hl), abs(hr))
        if hl < 0 or hr < 0 or abs(hl - hr) >= 2:
            h = -h
        return h
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        hl, hr = self.helper(root.left), self.helper(root.right)
        if hl >= 0 and hr >= 0 and abs(hl - hr) <= 1:
            return True
        return False
