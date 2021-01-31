from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 2:
            return True
        anchor, n = postorder[-1], len(postorder)
        i = 0
        while i < n - 1:
            if postorder[i] > anchor:
                break
            i += 1
        j = i
        while i < n - 1:
            if postorder[i] < anchor:
                return False
            i += 1
        return self.verifyPostorder(postorder[:j]) and self.verifyPostorder(postorder[j:n-1])