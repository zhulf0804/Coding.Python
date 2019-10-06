# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## 递归 + 记忆 （只用递归超时）
class Solution:
    def rob(self, root: TreeNode) -> int:
        d = {}
        def helper(root):
            if not root:
                return 0
            if root not in d:
                childcost = helper(root.left) + helper(root.right)
                curcost = root.val
                if root.left:
                    curcost += helper(root.left.left)
                    curcost += helper(root.left.right)
                if root.right:
                    curcost += helper(root.right.left)
                    curcost += helper(root.right.right)
                val = max(childcost, curcost)
                d[root] = val
            return d[root]
        return helper(root)


