# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return None, None
        a, b = root, root
        a1, b1 = self.helper(root.left)
        a2, b2 = self.helper(root.right)
        if a1:
            root.left = b1
            b1.right = root
            a = a1
        if a2:
            root.right = a2
            a2.left = root
            b = b2
        return a, b

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        head, tail = self.helper(root)
        tail.right = head
        head.left = tail
        return head

'''
特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
'''