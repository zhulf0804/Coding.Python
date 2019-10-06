# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                cur = cur.next
                continue
            pre.next = cur
            pre = cur
            cur = cur.next
        pre.next = None
        return dummy.next