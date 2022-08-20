# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def help(root, av):
            if not root:
                return av
            rv = help(root.right, av)
            root.val = root.val + rv
            lv = help(root.left, root.val)
            return lv
            
        help(root, 0)
        return root