'''
双队列: 一个是正常的队列，实现push_back()和pop_front(); 另一个队列用于辅助取队列的最大值.

辅助队列队头始终存放最大值元素(存放值还是索引呢，因为在pop_front时，
需要知道当前的最大值有没有被pop出去, 最好的方式是存储索引)

max_value: 取出辅助队列的队首元素
push_back(value): 正常队列，正常操作就好; 辅助队列需要取出队列中 <= value 的值, 并放入value的索引
pop_front: 正常队列正常操作即可; 辅助队列需要判断队首元素是否是pop的元素，若是则将其从辅助队列中弹出, 否则不变

此题目思路比较混乱，特此整理一下.

'''

class MaxQueue:

    def __init__(self):
        self.q = []
        self.idx = 0
        self.maxq = []
        self.idx1, self.idx2 = 0, -1

    def max_value(self) -> int:
        if self.idx1 > self.idx2:
            return -1
        v = self.q[self.maxq[self.idx1]]
        return v

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.idx2 >= self.idx1 and self.q[self.maxq[self.idx2]] <= value:
            self.idx2 -= 1
        self.idx2 += 1
        if self.idx2 < len(self.maxq):
            self.maxq[self.idx2] = len(self.q) - 1
        else:
            self.maxq.append(len(self.q) - 1)

    def pop_front(self) -> int:
        if self.idx >= len(self.q):
            return -1
        v = self.q[self.idx]
        if self.idx == self.maxq[self.idx1]:
            self.idx1 += 1
        self.idx += 1
        return v


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()