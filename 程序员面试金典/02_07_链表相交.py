# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        p = headA
        while p:
            lenA += 1
            p = p.next
        p = headB
        while p:
            lenB += 1
            p = p.next

        if lenB > lenA:
            headA, headB = headB, headA
        lenD = abs(lenB - lenA)
        p1, p2 = headA, headB
        while lenD > 0:
            p1 = p1.next
            lenD -= 1
        while lenA > 0:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None