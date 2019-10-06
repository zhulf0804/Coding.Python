from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTreeCore(new_preorder, new_inorder):
            if not new_preorder:
                return None
            root = TreeNode(new_preorder[0])
            loc = new_inorder.index(new_preorder[0])
            root.left = buildTreeCore(new_preorder[1:loc+1], new_inorder[:loc])
            root.right = buildTreeCore(new_preorder[loc+1:], new_inorder[loc+1:])
            return root
        return buildTreeCore(preorder, inorder)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
s.buildTree(preorder, inorder)