# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        pre, cur = head, head
        while k > 0:
            cur = cur.next
            k -= 1
        while cur:
            cur = cur.next
            pre = pre.next
        return pre.val