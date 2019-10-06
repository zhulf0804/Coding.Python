class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_0:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        out = []
        while l1 and l2:
            cur = l1.val + l2.val + carry
            carry = cur // 10
            out.append(cur % 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur = l1.val + carry
            carry = cur // 10
            out.append(cur % 10)
            l1 = l1.next
        while l2:
            cur = l2.val + carry
            carry = cur // 10
            out.append(cur % 10)
            l2 = l2.next
        if carry > 0:
            out.append(carry)
        res = ListNode(None)
        pre = res
        for val in out:
            cur_res = ListNode(val)
            pre.next = cur_res
            pre = cur_res
        return res.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        out = []
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            cur = val1 + val2 + carry
            carry = cur // 10
            out.append(cur % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            out.append(carry)
        res = ListNode(None)
        pre = res
        for val in out:
            cur_res = ListNode(val)
            pre.next = cur_res
            pre = cur_res
        return res.next