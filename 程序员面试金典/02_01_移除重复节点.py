# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        d = {}
        pre, cur = None, head
        while cur:
            if cur.val in d:
                pre.next = cur.next
            else:
                pre = cur
                d[cur.val] = 1
            cur = cur.next
        return head