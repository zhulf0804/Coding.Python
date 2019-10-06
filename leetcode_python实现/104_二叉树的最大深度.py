class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) ->int:
        def maxDepthCore(new_root):
            if not new_root:
                return 0
            return 1 + max(maxDepthCore(new_root.left), maxDepthCore(new_root.right))
        return maxDepthCore(root)
