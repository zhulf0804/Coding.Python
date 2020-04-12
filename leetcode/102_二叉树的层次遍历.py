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
        res = []
        tmp = []
        queue = []
        queue.append(root)
        cur_num = 1
        next_num = 0
        while queue:
            top = queue[0]
            tmp.append(top.val)
            queue = queue[1:]
            cur_num -= 1
            if top.left:
                queue.append(top.left)
                next_num += 1
            if top.right:
                queue.append(top.right)
                next_num += 1
            if cur_num == 0:
                res.append(tmp)
                tmp = []
                cur_num = next_num
                next_num = 0
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(root))

