from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, q, i = [], [root], 0
        level, cnt, nex = [], 1, 0
        while i < len(q):
            cur = q[i]
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
                nex += 1
            if cur.right:
                q.append(cur.right)
                nex += 1
            cnt -= 1
            if cnt == 0:
                res.append(level)
                level = []
                cnt = nex
                nex = 0
            i += 1
        return res