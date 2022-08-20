from ssl import HAS_NEVER_CHECK_COMMON_NAME


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        pre, cur = None, head2
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head2 = pre
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
            
        return True