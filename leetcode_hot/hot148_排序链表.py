# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List

# O(n^2) 复杂度超时
# class Solution:

#     def sortList(self, head):
#         if not head:
#             return head
        
#         next_head = self.sortList(head.next)
#         dummy = ListNode()
#         dummy.next = next_head
#         pre, cur = dummy, next_head
#         while cur:
#             if head.val > cur.val:
#                 pre = cur
#                 cur = cur.next
#             else:
#                 break
#         pre.next = head
#         head.next = cur
#         return dummy.next

class Solution:

    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        left = head
        left, right = self.sortList(left), self.sortList(right)

        # merge sorted left and right
        dummy = ListNode()
        p = dummy
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next

        if left:
            p.next = left
        if right:
            p.next = right
        return dummy.next
        