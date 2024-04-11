class MyHashSet:

    def __init__(self):
        self.hashs = set([])

    def add(self, key: int) -> None:
        self.hashs.add(key)

    def remove(self, key: int) -> None:
        self.hashs.discard(key)

    def contains(self, key: int) -> bool:
        if key in self.hashs:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)