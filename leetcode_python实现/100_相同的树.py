class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSameTreeCore(t1, t2):
            if not t1 and not t2:
                return True
            if not(t1 and t2):
                return False
            return t1.val == t2.val and isSameTreeCore(t1.left, t2.left) and isSameTreeCore(t1.right, t2.right)
        return isSameTreeCore(p, q)