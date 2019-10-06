# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 递归
class Solution_1:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        #if self.isValidBST(root.left) and self.isValidBST(root.right):
        def helper(root):
            mmax, mmin = root.val, root.val
            if root.left:
                flag, left_max, left_min = helper(root.left)
                if not flag or root.val <= left_max:
                    return False, 0, 0
                mmax = max(left_max, mmax)
                mmin = min(left_min, mmin)
            if root.right:
                flag, right_max, right_min = helper(root.right)
                if not flag or root.val >= right_min:
                    return False, 0, 0
                mmax = max(right_max, mmax)
                mmin = min(right_min, mmin)
            return True, mmax, mmin
        flag, _, _ = helper(root)
        return flag
# 递归
class Solution_2:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, upper=float('inf'), lower=float('-inf')):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            if not helper(root.left, upper, root.val):
                return False
            if not helper(root.right, root.val, lower):
                return False
            return True
        return helper(root)

# 迭代
class Solution_3:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        stack.append([root, float('-inf'), float('inf')])
        while stack:
            node, lower, upper = stack.pop()
            val = node.val
            if val <= lower or val >= upper:
                return False
            if node.right:
                stack.append([node.right, val, upper])
            if node.left:
                stack.append([node.left, lower, val])
        return True

# 中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack, inorder = [], float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= inorder:
                return False
            inorder = node.val
            if node.right:
                root = node.right
        return True






