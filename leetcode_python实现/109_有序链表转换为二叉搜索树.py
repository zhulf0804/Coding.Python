#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head

        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next

        def sortedListToBST(new_sorted_list):
            if not new_sorted_list:
                return None
            mid = len(new_sorted_list) // 2
            root = TreeNode(new_sorted_list[mid])
            root.left = sortedListToBST(new_sorted_list[:mid])
            root.right = sortedListToBST(new_sorted_list[mid+1:])
            return root
        return sortedListToBST(sorted_list)
