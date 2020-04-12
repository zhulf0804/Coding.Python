# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        target = None
        pre_target = None
        i = 1
        while cur:
            tmp = cur.next
            if i == m:
                target = cur
                pre_target = pre
            if i > m and i <= n:
                cur.next = pre

            if i == n:
                pre_target.next = cur
                target.next = tmp
                break
            pre = cur
            cur = tmp
            i += 1
        return dummy.next


