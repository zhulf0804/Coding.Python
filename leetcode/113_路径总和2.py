from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def pathSumCore(new_root, new_sum, cur):
            if not new_root:
                return
            if not new_root.left and not new_root.right:
                if new_root.val == new_sum:
                    res.append(cur + [new_root.val])
            if new_root.left:
                pathSumCore(new_root.left, new_sum - new_root.val, cur + [new_root.val])
            if new_root.right:
                pathSumCore(new_root.right, new_sum - new_root.val, cur + [new_root.val])
        pathSumCore(root, sum, [])
        return res
