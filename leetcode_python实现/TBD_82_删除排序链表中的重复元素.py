# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while pre.next:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur = cur.next
        return dummy.next