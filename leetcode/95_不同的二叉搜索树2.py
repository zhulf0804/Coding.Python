from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(lst):
            if not lst:
                return [None]
            roots = []
            for i in range(len(lst)):
                lefts = helper(lst[:i])
                rights = helper(lst[i + 1:])
                for left in lefts:
                    for right in rights:
                        root = TreeNode(lst[i])
                        root.left = left
                        root.right = right
                        roots.append(root)
            return roots
        return helper([i for i in range(1, n+1)]) if n > 0 else []

s = Solution()
print(s.generateTrees(3))

