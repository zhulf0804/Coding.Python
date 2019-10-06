# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        need = head
        cur = head.next
        pre = head
        i = 2
        while cur:
            if i % 2 == 1:
                tmp1 = need.next
                tmp2 = cur.next
                need.next = cur
                cur.next = tmp1
                need = cur
                pre.next = tmp2
                cur = tmp2
            else:
                pre = cur
                cur = cur.next

            i += 1
        return head
