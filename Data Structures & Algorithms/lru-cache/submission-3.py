class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        del self.hashmap[node.key]
        

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        self.hashmap[node.key] = node



        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            val = self.hashmap[key].val
            self.remove(self.hashmap[key])
            self.insert(Node(key,val))
            return self.hashmap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        self.insert(node)
        # self.hashmap[key] = node
        if len(self.hashmap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            




        
