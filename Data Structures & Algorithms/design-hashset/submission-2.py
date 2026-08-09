class MyHashSet:

    def __init__(self):
        self.hashset = []


    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)
        

    def remove(self, key: int) -> None:
        self.hashset.remove(key) if key in self.hashset else None
        

    def contains(self, key: int) -> bool:
        for i in self.hashset:
            if i == key:
                return True
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)