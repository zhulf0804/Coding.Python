class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def inorderTraversal(self, root):
#         if not root:
#             return []
    
#         left_res = self.inorderTraversal(root.left)
#         right_res = self.inorderTraversal(root.right)
#         results = left_res + [root.val] + right_res
#         return results


class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
