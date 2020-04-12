# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        k = k % l
        fast = head
        step = 0
        while step < k:
            step += 1
            fast = fast.next
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        if not slow.next:
            return head
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

