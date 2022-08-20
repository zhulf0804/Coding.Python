class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def core(root):
            if not root:
                return True, None, None
            left, left_max, left_min = core(root.left)
            right, righ_max, right_min = core(root.right)

            if left and right:
                if left_max is None and right_min is None:
                    return True, root.val, root.val
                elif left_max is None and right_min is not None:
                    return root.val < right_min, righ_max, root.val
                elif left_max is not None and right_min is None:
                    return root.val > left_max, root.val, left_min
                else:
                    return root.val > left_max and root.val < right_min, righ_max, left_min
                
            return False, None, None
        ans, max, min =  core(root)
        return ans
