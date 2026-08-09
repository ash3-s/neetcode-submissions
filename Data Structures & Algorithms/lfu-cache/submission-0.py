class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next 

class LinkedList:
    def __init__(self):
        self.left, self.right = ListNode(0, None, None), ListNode(0, None, None)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}

    def length(self):
        return len(self.map)



    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
            self.map.pop(val, None)
            

    def pushRight(self, val):
        node = ListNode(val)
        self.map[val] = node
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    
    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCount = 0
        self.valMap = {}
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)
    
    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if self.lfuCount == cnt and self.listMap[cnt].length() == 0:
            self.lfuCount += 1
        

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 
        
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCount].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
        
        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)