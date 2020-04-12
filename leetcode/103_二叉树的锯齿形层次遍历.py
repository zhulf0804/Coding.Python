from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def search(childroot, depth):
            if not childroot:
                return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:
                res[depth].append(childroot.val)
            else:
                res[depth].insert(0, childroot.val)
            search(childroot.left, depth + 1)
            search(childroot.right, depth + 1)
        search(root, 0)
        return res

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack1 = []
        stack2 = []
        ind = 0
        stack1.append(root)
        while stack1 or stack2:
            if stack1:
                res.append([])
            while stack1:
                top = stack1.pop()
                res[ind].append(top.val)
                if top.left:
                    stack2.append(top.left)
                if top.right:
                    stack2.append(top.right)
            ind += 1
            if stack2:
                res.append([])
            while stack2:
                top = stack2.pop()
                res[ind].append(top.val)
                if top.right:
                    stack1.append(top.right)
                if top.left:
                    stack1.append(top.left)
            ind += 1
        return res



