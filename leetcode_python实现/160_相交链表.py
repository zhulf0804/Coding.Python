# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur = headA
        lenA = 0
        while cur:
            lenA += 1
            cur = cur.next

        lenB = 0
        cur = headB
        while cur:
            lenB += 1
            cur = cur.next

        curA = headA
        curB = headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        else:
            for i in range(lenB - lenA):
                curB = curB.next

        while curA and curB:
            if curA == curB:
                return curB
            curA = curA.next
            curB = curB.next
        return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB  else headA
        return curA