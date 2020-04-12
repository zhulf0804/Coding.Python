# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.num = 0
        def converBSTCore(childroot):
            if not childroot:
                return
            converBSTCore(childroot.right)
            self.num += childroot.val
            childroot.val = self.num
            converBSTCore(childroot.left)
        converBSTCore(root)
        return root
