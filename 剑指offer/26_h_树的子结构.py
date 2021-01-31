# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root):
        if not root:
            return []
        return [root] + self.preOrder(root.left) + self.preOrder(root.right)
    def judge(self, Father, Child):
        if not Child:
            return True
        if not Father:
            return False
        if Father.val != Child.val:
            return False
        return self.judge(Father.left, Child.left) and self.judge(Father.right, Child.right)
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        LA = self.preOrder(A)
        for root in LA:
            if self.judge(root, B):
                return True
        return False

'''
[10,12,6,8,3,11]
[10,12,6,8]
'''

'''
[10, 12, 8, 3, 6, 11] [10, 12, 8, 6]

'''