# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        p = head
        g = []
        l = []
        while p:
            if p.val < x:
                l.append(p.val)
            else:
                g.append(p.val)
            p = p.next
        p = head
        i = 0
        j = 0
        while p:
            if i < len(l):
                p.val = l[i]
                i += 1
            else:
                p.val = g[j]
                j += 1
            p = p.next
        return head
