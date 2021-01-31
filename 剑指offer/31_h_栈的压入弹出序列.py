'''
独立写出:
遍历popped序列，对于popped[j]，判断是否已在已访问的序列(s_v)中，
- 若不在，则表示合法, 同时从pushed序列中插入若干元素到s_v中
- 若存在,
  - 若其为最后一个元素, 则合法，j += 1
  - 否则不合法
'''

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j, n = 0, 0, len(pushed)
        s_v = []
        for j in range(n):
            k = 0
            while k < len(s_v):
                if s_v[k] == popped[j]:
                    break
                k += 1
            if k == len(s_v) - 1:
                s_v.pop()
                continue
            elif k < len(s_v) - 1:
                return False
            else:
                while i < n and pushed[i] != popped[j]:
                    s_v.append(pushed[i])
                    i += 1
                i += 1
        return True

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
a = Solution()
print(a.validateStackSequences(pushed, popped))