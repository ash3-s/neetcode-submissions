class TimeMap:

    def __init__(self): 
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = []
        if self.hashmap[key]:
            arr = self.hashmap[key]
        
        l, r = 0, len(arr) - 1
        v = ""
        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                v = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return v
