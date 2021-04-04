# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def in_order(self, root):
        if not root:
            return []
        left = self.in_order(root.left)
        cur = [root.val]
        right = self.in_order(root.right)
        return left + cur + right

    def isValidBST(self, root: TreeNode) -> bool:
        nodes = self.in_order(root)
        for i in range(1, len(nodes)):
            if nodes[i-1] >= nodes[i]:
                return False
        return True
