class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isSymmetricCore(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isSymmetricCore(left.left, right.right) and isSymmetricCore(left.right, right.left)

        return isSymmetricCore(root.left, root.right)