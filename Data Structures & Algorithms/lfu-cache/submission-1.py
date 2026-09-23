class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.nodeMap = {}
        self.left, self.right = ListNode(0), ListNode(0)
        self.left.next, self.right.prev = self.right, self.left

    def length(self):
        return len(self.nodeMap)
    
    def pop(self, val):
        if val in self.nodeMap:
            node = self.nodeMap[val]
            prev, nxt = node.prev, node.next
            prev.next, nxt.prev = nxt, prev
            self.nodeMap.pop(val)

    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.nodeMap[val] = node
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valMap = defaultdict(int)
        self.lfuCount = 0
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCount and self.listMap[cnt].length() == 0:
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