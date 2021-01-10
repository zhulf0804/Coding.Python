# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p, num = copy.deepcopy(head), 0
        l, r = None, None
        while p:
            num += 1
            if num == k:
                l = copy.deepcopy(p)
            p = p.next
        k = num - k + 1
        num = 0
        while p:
            num += 1
            if num == k:
                r = copy.deepcopy(p)
                break
            p = p.next
        l.val, r.val = r.val, l.val
        return head

head = [1,2,3,4,5]
k = 2
a = Solution()
head = a.swapNodes(head, k)
while head:
    print(head.val)
    head = head.next
