class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def core(self, root):
        if not root:
            return root, root
        left_head, left_tail = self.core(root.left)
        right_head, right_tail = self.core(root.right)
        if left_head is None and right_head is None:
            return root, root
        if left_head is not None and right_head is None:
            root.left = None
            root.right = left_head
            return root, left_tail
        if left_head is None and right_head is not None:
            root.right = right_head
            return root, right_tail
        root.right = left_head
        root.left = None
        left_tail.right = right_head
        return root, right_tail
        
    def flatten(self, root):
        root, _ = self.core(root)
        return root
        