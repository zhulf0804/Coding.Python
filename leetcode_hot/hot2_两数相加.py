class ListNode:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l = ListNode()
        p, q, r = l1, l2, l
        add = 0
        while p and q:
            cur = p.val + q.val
            r.val = (cur + add) % 10
            add = (cur + add) // 10
            if add > 0 or p.next or q.next:
                r.next = ListNode()
                r = r.next
            p = p.next
            q = q.next
        while p:
            r.val = (p.val + add) % 10
            add = (p.val + add) // 10 
            if add > 0 or p.next:
                r.next = ListNode()
                r = r.next
            p = p.next
        while q:
            r.val = (q.val + add) % 10
            add = (q.val + add) // 10 
            if add > 0 or q.next:
                r.next = ListNode()
                r = r.next
            q = q.next
        
        if add > 0:
            r.val = add

        return l