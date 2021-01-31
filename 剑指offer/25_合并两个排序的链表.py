# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        DumP = ListNode(0)
        p, p1, p2 = DumP, l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        while p1:
            p.next = p1
            p1 = p1.next
            p = p.next
        while p2:
            p.next = p2
            p2 = p2.next
            p = p.next
        return DumP.next