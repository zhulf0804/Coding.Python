# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        cur, pre = slow.next, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        half = head
        while pre:
            if pre.val != half.val:
                return False
            pre = pre.next
            half = half.next
        return True
