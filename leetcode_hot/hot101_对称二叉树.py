class Solution:
    def isSymmetricCore(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        if root1.val != root2.val:
            return False
        l = self.isSymmetricCore(root1.left, root2.right)
        r = self.isSymmetricCore(root1.right, root2.left)
        return l and r

    def isSymmetric(self, root):
        root1, root2 = root.left, root.right
        return self.isSymmetricCore(root1, root2)
