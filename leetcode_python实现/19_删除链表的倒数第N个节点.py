# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_p = None
        cur_p = head
        quick_p = head
        k = 0
        while k < n:
            quick_p = quick_p.next
            k += 1
        while quick_p:
            quick_p = quick_p.next
            pre_p = cur_p
            cur_p = cur_p.next
        if pre_p is None:
            return cur_p.next
        pre_p.next = cur_p.next
        return head