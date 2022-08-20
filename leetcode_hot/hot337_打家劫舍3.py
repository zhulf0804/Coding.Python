class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def __init__(self):
#         self.res = {}
#     def rob(self, root):
#         if not root:
#             return 0
#         if root in self.res:
#             return self.res[root]

#         v1 = root.val
#         if root.left:
#             v1 += self.rob(root.left.left)
#             v1 += self.rob(root.left.right)
#         if root.right:
#             v1 += self.rob(root.right.left)
#             v1 += self.rob(root.right.right)
        
#         v2 = self.rob(root.left) + self.rob(root.right)
#         v = max(v1, v2)
#         self.res[root] = v
#         return v

class Solution:
    def rob(self, root):
        def helper(root):
            if not root:
                return 0, 0
            l = helper(root.left)
            r = helper(root.right)
            selected = root.val + l[1] + r[1]
            notSelected = max(l) + max(r)
            return selected, notSelected
        return max(helper(root))
    