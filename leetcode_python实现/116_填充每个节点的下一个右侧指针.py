"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = []
        queue.append(root)
        cur_num = 1
        next_num = 0
        while queue:
            top = queue.pop(0)
            cur_num -= 1
            if cur_num > 0:
                top.next = queue[0]
            if top.left:
                queue.append(top.left)
                next_num += 1
            if top.right:
                queue.append(top.right)
                next_num += 1
            if cur_num == 0:
                cur_num = next_num
                next_num = 0
        return root