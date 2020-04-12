# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        pre = None
        while slow:
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        cur1 = head
        cur2 = pre
        while cur2:
            if cur2.val == cur1.val:
                cur1 = cur1.next
                cur2 = cur2.next
                continue
            else:
                return False
        return True
