# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        p1, p2, p = l1, l2, l
        base = 0
        while p1 or p2:
            if p1 and p2:
                cur = (base + p1.val + p2.val) % 10
                base = (base + p1.val + p2.val) // 10
                p1.val = cur
                p.next = p1
                p1 = p1.next
                p2 = p2.next
            elif p1 and not p2:
                cur = (base + p1.val) % 10
                base = (base + p1.val) // 10
                p1.val = cur
                p.next = p1
                p1 = p1.next
            elif not p1 and p2:
                cur = (base + p2.val) % 10
                base = (base + p2.val) // 10
                p2.val = cur
                p.next = p2
                p2 = p2.next
            p = p.next
        if base != 0:
            p.next = ListNode(base)
        return l.next
