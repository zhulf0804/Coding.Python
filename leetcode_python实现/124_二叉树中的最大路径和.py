# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        def helper(root):
            if not root:
                return 0, 0
            left1, right1 = helper(root.left)
            left2, right2 = helper(root.right)
            cur = root.val + max([0, left1, right1]) + max([0, left2, right2])
            # print(root.val, left1, right1, left2, right2)
            if cur > self.res:
                self.res = cur
            return max([left1, right1, 0]) + root.val, max([left2, right2, 0]) + root.val
        helper(root)
        return self.res

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.maxPathSum(root))