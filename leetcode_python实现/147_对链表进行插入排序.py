# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = head.next
        head.next = None
        while cur:
            pre = dummy
            now = dummy.next
            while now and now.val < cur.val:
                pre = now
                now = now.next
            tmp = cur.next
            pre.next = cur
            cur.next = now
            cur = tmp
        return dummy.next

