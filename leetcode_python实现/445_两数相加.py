# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(l):
            pre = None
            cur = l
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        l1 = reverseList(l1)
        l2 = reverseList(l2)

        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode(-1)
        cur = dummy
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            summ = val1 + val2 + carry
            carry = summ // 10
            cur.next = ListNode(summ % 10)
            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        if carry > 0:
            cur.next = ListNode(carry)
        return reverseList(dummy.next)


