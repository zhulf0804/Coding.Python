# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.paths = []
        def findPath(childroot, cur):
            if not childroot or len(self.paths) == 2:
                return
            cur = cur + [childroot]
            if childroot == p or childroot == q:
                self.paths.append(cur)
            findPath(childroot.left, cur)
            findPath(childroot.right, cur)
        findPath(root, [])
        res = None
        mmin = min(len(self.paths[0]), len(self.paths[1]))
        for i in range(mmin):
            if self.paths[0][i] == self.paths[1][i]:
                res = self.paths[0][i]
            else:
                break
        return res

class Solution_2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
