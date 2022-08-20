from torch import ne


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        if not fast:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        nextp = slow.next
        slow.next = nextp.next
        return head