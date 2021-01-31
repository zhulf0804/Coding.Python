# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        d = {}
        L = Node(head.val)
        d[head] = L
        p1, p2 = head, L
        while p1.next:
            p1 = p1.next
            newNode = Node(p1.val)
            d[p1] = newNode
            p2.next = newNode
            p2 = p2.next
        p1, p2 = head, L
        while p1:
            if p1.random:
                p2.random = d[p1.random]
            p1 = p1.next
            p2 = p2.next
        return L


'''
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
'''