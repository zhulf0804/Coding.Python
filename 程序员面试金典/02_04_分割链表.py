# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        headA, headB = ListNode(0), ListNode(0)
        pa, pb, p = headA, headB, head
        while p:
            if p.val < x:
                pa.next = p
                pa = pa.next
            else:
                pb.next = p
                pb = pb.next
            p = p.next
        pa.next = headB.next
        pb.next = None
        return headA.next
