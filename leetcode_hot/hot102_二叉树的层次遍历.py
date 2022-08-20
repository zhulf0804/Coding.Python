class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        cur, res = [], []
        queue = [root]
        ncur, next = 1, 0
        while queue:
            root = queue.pop(0)
            ncur -= 1
            cur.append(root.val)
            if root.left:
                next += 1
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
                next += 1
            
            if ncur == 0:
                res.append(cur)
                cur = []
                ncur = next
                next = 0
        return res