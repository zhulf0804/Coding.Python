"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        max_depth = 0
        for item in root.children:
            max_depth = max(max_depth, 1 + self.maxDepth(item))
        return max_depth