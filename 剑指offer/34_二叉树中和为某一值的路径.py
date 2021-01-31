from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, cur, summ, target, res):
        if not root.left and not root.right:
            if summ + root.val == target:
                res.append(cur + [root.val])
            return
        if root.left:
            self.helper(root.left, cur + [root.val], summ + root.val, target, res)
        if root.right:
            self.helper(root.right, cur + [root.val], summ + root.val, target, res)
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.helper(root, [], 0, sum, res)
        return res