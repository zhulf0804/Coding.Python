from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #print(inorder)
        #print(postorder)
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        loc = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:loc], postorder[:loc])
        root.right = self.buildTree(inorder[loc+1:], postorder[loc:-1])
        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
s = Solution()
res = s.buildTree(inorder, postorder)
print(res)