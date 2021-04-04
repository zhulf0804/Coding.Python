from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        q, cur, next = [tree], 1, 0
        i = 0
        results, result = [[tree.val]], []
        while i < len(q):
            node = q[i]
            if node.left:
                next += 1
                q.append(node.left)
                result.append(node.left.val)
            if node.right:
                next += 1
                q.append(node.right)
                result.append(node.right.val)
            cur -= 1
            if cur == 0:
                results.append(result)
                result = []
                cur = next
                next = 0
            i += 1
        results_list = []
        for i in range(len(results)):
            result = results[i]
            if len(result) > 0:
                head = ListNode(result[0])
                p = head
                for i in range(1, len(result)):
                    p.next = ListNode(result[i])
                    p = p.next
                results_list.append(head)
        return results_list
