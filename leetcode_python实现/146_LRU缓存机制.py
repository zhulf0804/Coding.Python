from collections import OrderedDict
## 超时
class LRUCache_1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = 0
        self.cache = {}
        self.key2time = {}
        self.time2key = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        time = self.key2time[key]
        for i in range(time-1, -1, -1):
            key0 = self.time2key[i]
            self.key2time[key0] += 1
            self.time2key[self.key2time[key0]] = key0

        self.key2time[key] = 0
        self.time2key[0] = key
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            time = self.key2time[key]
            for i in range(time-1, -1, -1):
                key0 = self.time2key[i]
                self.key2time[key0] += 1
                self.time2key[self.key2time[key0]] = key0
            self.key2time[key] = 0
            self.time2key[0] = key
            return
        if self.index < self.capacity:
            self.cache[key] = value
            for i in range(self.index-1, -1, -1):
                key0 = self.time2key[i]
                self.time2key.pop(i)
                self.key2time[key0] += 1
                self.time2key[self.key2time[key0]] = key0
            self.key2time[key] = 0
            self.time2key[0] = key
            self.index += 1
        else:
            max_key = self.time2key[self.capacity - 1]
            self.cache.pop(max_key)
            self.key2time.pop(max_key)
            self.time2key.pop(self.capacity - 1)
            for i in range(self.capacity - 2, -1, -1):
                key0 = self.time2key[i]
                self.key2time[key0] += 1
                self.time2key.pop(i)
                self.time2key[self.key2time[key0]] = key0
            self.cache[key] = value
            self.time2key[0] = key
            self.key2time[key] = 0
        return

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.update(key)
        self.lru.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self.update(key)
        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(False)

    def update(self, key: int):
        if key in self.lru:
            self.lru.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)