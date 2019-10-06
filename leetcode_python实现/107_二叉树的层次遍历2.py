from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        level = []
        cur = 1
        next = 0
        while queue:
            front = queue.pop(0)
            cur -= 1
            level.append(front.val)
            if front.left:
                queue.append(front.left)
                next += 1
            if front.right:
                queue.append(front.right)
                next += 1
            if cur == 0:
                res.append(level)
                level = []
                cur = next
                next = 0
        return res[::-1]