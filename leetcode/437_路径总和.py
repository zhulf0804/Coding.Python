import numpy as np
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        def helper(root, cur):
            if not root:
                return
            if cur:
                cur = [item + root.val for item in cur]
            cur.append(root.val)
            self.res += np.sum(np.array(cur) == sum)
            helper(root.left, cur)
            helper(root.right, cur)
        helper(root, [])
        return self.res

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)

obj = Solution()
print(obj.pathSum(root, 10))