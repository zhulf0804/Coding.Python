# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层次遍历
class Solution_1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        cur_height = 1
        cur = 1
        next = 0
        queue = []
        queue.append(root)
        while queue:
            front = queue[0]
            queue = queue[1:]
            cur -= 1
            if not front.left and not front.right:
                break
            if front.left:
                queue.append(front.left)
                next += 1
            if front.right:
                queue.append(front.right)
                next += 1
            if cur == 0:
                cur_height += 1
                cur = next
                next = 0
        return cur_height

# 递归
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        hl = self.minDepth(root.left)
        hr = self.minDepth(root.right)

        return hl + hr + 1 if not root.left or not root.right else min(hl, hr) + 1


