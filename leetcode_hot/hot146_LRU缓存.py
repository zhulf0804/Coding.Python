class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {}

    def get(self, key):
        v = -1
        if key in self.hash_map:
            v = self.hash_map[key].value
            self.move_to_end(key, v)
        return v

    def put(self, key, value):
        self.move_to_end(key, value)
        if len(self.hash_map) > self.capacity:
            self.head = self.head.next
            self.hash_map.pop(self.head.key)

    def move_to_end(self, key, v=None):
        node = ListNode(key, v)

        if key in self.hash_map:
            node = self.hash_map[key]
            if v is not None:
                node.value = v
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        else:
            self.hash_map[key] = node
        
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail
