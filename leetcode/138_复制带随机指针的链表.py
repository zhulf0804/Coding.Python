"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

# 利用辅助字典
class Solution_1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        dummy = Node(-1, None, None)
        cp_cur = dummy
        d = {}
        while cur:
            cp_cur.next = Node(cur.val, None, None)
            cp_cur = cp_cur.next
            d[cur] = cp_cur
            cur = cur.next
        cur, cp_cur = head, dummy.next
        while cur:
            if cur.random:
                cp_cur.random = d[cur.random]
            cp_cur = cp_cur.next
            cur = cur.next
        return dummy.next

# 不适用辅助字典
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        while cur:
            next = cur.next
            cur.next = Node(cur.val, cur.next, None)
            cur = next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        dummy = Node(-1, None, None)
        cp_cur = dummy
        cur = head
        while cur:
            cp_cur.next = cur.next
            cur.next = cur.next.next
            cp_cur = cp_cur.next
            cur = cur.next
        return dummy.next


