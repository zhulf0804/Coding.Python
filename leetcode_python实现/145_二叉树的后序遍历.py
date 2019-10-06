from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution_1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []

        def postorderTraversalCore(new_root):
            if not new_root:
                return
            postorderTraversalCore(new_root.left)
            postorderTraversalCore(new_root.right)
            res.append(new_root.val)
        postorderTraversalCore(root)
        return res

# 非递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            top = stack[-1]
            stack = stack[:-1]
            res.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return res[::-1]

