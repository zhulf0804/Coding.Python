from typing import List
from queue import PriorityQueue
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
## 基本想法
class Solution_1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        def merge2Lists(list1, list2):
            dummy = ListNode(-1)
            cur = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if list1:
                cur.next = list1
            if list2:
                cur.next = list2
            return dummy.next
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge2Lists(res, lists[i])
        return res

## 优先队列
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(-1)
        q = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i, l))

        while not q.empty():
            val, i, node = q.get()
            point.next = node
            node = node.next
            if node:
                q.put((node.val, i, node))
        return head.next
