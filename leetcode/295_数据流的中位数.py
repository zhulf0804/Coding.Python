class MedianFinder_1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.len = 0

    def addNum(self, num: int) -> None:
        l, r = 0, self.len - 1
        # 寻找第一个比 num 大的位置
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] <= num:
                l = mid + 1
            else:
                r = mid
        if self.len > 0 and self.nums[l] < num:
            l += 1
        self.nums.insert(l, num)
        self.len += 1
    def findMedian(self) -> float:
        if self.len % 2 == 1:
            return self.nums[self.len // 2]
        else:
            return (self.nums[self.len // 2] + self.nums[self.len // 2 - 1]) / 2
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self) -> float:
        if self.count & 1:
            return self.max_heap[0][1]
        return (self.max_heap[0][1] + self.min_heap[0]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()