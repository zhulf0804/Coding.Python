# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         l1, l2 = 0, 0
#         p = headA
#         while p:
#             l1 += 1
#             p = p.next
#         q = headB
#         while q:
#             l2 += 1
#             q = q.next
        
#         if l1 > l2:
#             l1, l2 = l2, l1
#             headA, headB = headB, headA
        
#         l = abs(l1 - l2)
#         q = headB
#         while l > 0:
#             q = q.next
#             l -= 1
#         p = headA
#         while p:
#             if p == q:
#                 return p
#             p = p.next
#             q = q.next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
