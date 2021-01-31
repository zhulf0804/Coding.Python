from typing import List

class Solution:
    def partition(self, arr, l, r):
        pivot = arr[r]
        i, j = l, r
        while i < j:
            while i < j and arr[i] < pivot:
                i += 1
            while j > i and arr[j] >= pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[i], arr[r] = arr[r], arr[i]  # 把pivot放在分解出比较重要
        return i

    def quickSearch(self, arr, l, r, k):
        i = self.partition(arr, l, r)
        if i == k:
            return arr[:(k+1)]
        elif i > k:
            return self.quickSearch(arr, l, i-1, k)
        else:
            return self.quickSearch(arr, i+1, r, k)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0 or not arr:
            return []
        res = self.quickSearch(arr, 0, len(arr) - 1, k-1)
        return res
