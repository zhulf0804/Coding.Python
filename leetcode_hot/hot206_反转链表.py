class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return head
        p, q = None, head
        while q:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        return p