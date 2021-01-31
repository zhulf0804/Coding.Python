# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getDepth(self, root):
        if not root:
            return 0
        deptha, depthb = self.getDepth(root.left), self.getDepth(root.right)
        if deptha == -1 or depthb == -1:
            return -1
        if abs(deptha - depthb) > 1:
            return -1
        return 1 + max(deptha, depthb)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        deptha, depthb = self.getDepth(root.left), self.getDepth(root.right)
        if deptha == -1 or depthb == -1:
            return False
        if abs(deptha - depthb) > 1:
            return False
        return True