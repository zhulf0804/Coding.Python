# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0,  0
        p = headA
        while p:
            p = p.next
            lenA += 1
        p = headB
        while p:
            p = p.next
            lenB += 1
        pa, pb = headA, headB
        if lenA < lenB:
            pa, pb = headB, headA
        i = 0
        while i < abs(lenA - lenB):
            i += 1
            pa = pa.next
        while pa and pa != pb:
            pa = pa.next
            pb = pb.next
        return pa
