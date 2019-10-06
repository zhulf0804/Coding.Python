# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_core(child_root):
            if not child_root:
                return None
            if not child_root.left and not child_root.right:
                return child_root
            left_root = child_root.left
            right_root = child_root.right
            if left_root:
                tail = flatten_core(left_root)
                child_root.right = left_root
                tail.right = right_root
            if right_root:
                tail = flatten_core(right_root)
            child_root.left = None
            return tail
        flatten_core(root)
        #print(root.val, root.right.val, root.right.right.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
s = Solution()
print(s.flatten(root))

