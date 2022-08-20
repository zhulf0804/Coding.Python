# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. 递归
# class Solution:
#     def merge2Lists(self, list1, list2):
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1.val < list2.val:
#             tmp = self.merge2Lists(list1.next, list2)
#             list1.next = tmp
#             return list1
#         else:
#             tmp = self.merge2Lists(list1, list2.next)
#             list2.next = tmp
#             return list2
#     def mergeKLists(self, lists):
#         n = len(lists)
#         if n == 0:
#             return None
#         res_link = lists[0]
#         for i in range(n-1):
#             res_link = self.merge2Lists(res_link, lists[i+1])
#         return res_link

# 2. 非递归
from typing import List


class Solution:
    def merge2Lists(self, list1, list2):
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2= list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next

    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0:
            return None
        res_link = lists[0]
        for i in range(n-1):
            res_link = self.merge2Lists(res_link, lists[i+1])
        return res_link

# 3. 优先队列
# from queue import PriorityQueue as PQ

# class Solution:
#     def mergeKLists(self, lists):
#         n = len(lists)
#         if n == 0:
#             return None
#         dummy = ListNode()
#         cur = dummy
#         pq = PQ()
#         for i in range(n):
#             if lists[i]:
#                 pq.put((lists[i].val, i, lists[i]))
        
#         while not pq.empty():
#             _, i, l = pq.get()
#             cur.next = l
#             cur = cur.next
#             if l.next:
#                 pq.put((l.next.val, i, l.next))

#         return dummy.next
