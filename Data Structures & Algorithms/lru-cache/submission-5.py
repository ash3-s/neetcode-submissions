class Node:
    def __init__(self, key, val=0, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0), Node(0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def removeFromCache(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next = nxt
        node.next.prev = prev
    def addToCache(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = self.right.prev = node
        node.prev = prev
        node.next = nxt
    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeFromCache(self.cache[key])
            self.addToCache(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeFromCache(self.cache[key])

        self.cache[key] = Node(key, value)
        self.addToCache(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.removeFromCache(lru)
            del self.cache[lru.key]
