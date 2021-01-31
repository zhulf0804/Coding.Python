# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def compare(self, childA, childB):
        if not childA and not childB:
            return True
        if not childA or not childB:
            return False
        if childA.val != childB.val:
            return False
        return self.compare(childA.left, childB.right) \
               and self.compare(childA.right, childB.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)