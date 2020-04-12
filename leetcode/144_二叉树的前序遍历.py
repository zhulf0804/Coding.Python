from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution_1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorderTraversalCore(new_root):
            if not new_root:
                return
            res.append(new_root.val)
            preorderTraversalCore(new_root.left)
            preorderTraversalCore(new_root.right)
        preorderTraversalCore(root)
        return res

# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)

        while stack:
            top = stack[-1]
            res.append(top.val)
            stack = stack[:-1]
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return res