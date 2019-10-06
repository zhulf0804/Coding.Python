# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
## 超时
class Solution_1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def recorderListCore(new_head):
            if not new_head or not new_head.next or not new_head.next.next:
                return new_head
            pre = new_head
            cur = new_head.next
            while cur.next:
                pre = cur
                cur = cur.next
            tmp = new_head.next
            new_head.next = cur
            pre.next = None
            cur.next = recorderListCore(tmp)
            return new_head
        dummy = ListNode(-1)
        dummy.next = recorderListCore(head)
        return dummy.next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None

        cur = mid
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        a = head
        b = pre
        while b:
            tmpa = a.next
            a.next = b
            tmpb = b.next
            b.next = tmpa
            a = tmpa
            b = tmpb
        return a

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
s.reorderList(head)