# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head
        cycle = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle = True
                break
        if not cycle:
            return None
        p1, p2 = head, slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
