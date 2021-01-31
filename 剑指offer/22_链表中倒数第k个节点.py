# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre, cur = head, head
        i = 0
        while i < k:
            i += 1
            cur = cur.next
        while cur:
            pre = pre.next
            cur = cur.next
        return pre