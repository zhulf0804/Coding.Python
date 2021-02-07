'''
此次做这个题目，只想到了，插入O(1)，寻找中值O(nlogn)的想法
翻看了2020年下半年的刷的leetcode，看到当时还想到了插入O(n), 寻找中值O(1)的想法，退步了?

上述两个算法都不能ac，ac的算法是基于大顶堆/小顶堆的, 插入O(logn), 查找O(1)
python中由于没有大顶堆，因此需要插入相反数/取出后相反数.
'''

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap, self.min_heap = [], []
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count & 1 == 1:
            heapq.heappush(self.max_heap, -num)
            v = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, v)
        else:
            heapq.heappush(self.min_heap, num)
            v = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -v)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()