# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 中序遍历并保存结果
class Solution_1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        vals = []
        def inOrder(childroot):
            if not childroot:
                return
            inOrder(childroot.left)
            vals.append(childroot.val)
            inOrder(childroot.right)
        inOrder(root)
        return vals[k-1]

class Solution_2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cur = 0
        self.val = 0
        def inorder_search(childroot):
            if not childroot or self.cur > k:
                return
            inorder_search(childroot.left)
            self.cur += 1
            if self.cur == k:
                self.val = childroot.val
                return
            inorder_search(childroot.right)
        inorder_search(root)
        return self.val

# 栈实现中序遍历
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        ind = 0
        while stack:
            top = stack.pop(-1)
            ind += 1
            if k == ind:
                return top.val
            if top.right:
                cur = top.right
                while cur:
                    stack.append(cur)
                    cur = cur.left


