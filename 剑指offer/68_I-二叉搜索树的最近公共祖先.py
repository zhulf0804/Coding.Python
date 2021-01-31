# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, p, nodes):
        if not root:
            return False
        if root == p:
            nodes.append(root)
            return True
        if self.helper(root.left, p, nodes) or self.helper(root.right, p,
                                                           nodes):
            nodes.append(root)
            return True
        return False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes1, nodes2 = [], []
        self.helper(root, p, nodes1)
        self.helper(root, q, nodes2)
        nodes1, nodes2 = list(reversed(nodes1)), list(reversed(nodes2))
        i = 0
        while i < min(len(nodes1), len(nodes2)):
            if nodes1[i] != nodes2[i]:
                return nodes1[i - 1]
            i += 1
        return nodes1[i - 1]

'''
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中
'''