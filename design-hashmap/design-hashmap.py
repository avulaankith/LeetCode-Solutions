class MyHashMap:

    def __init__(self):
        self.hashs = {}

    def put(self, key: int, value: int) -> None:
        self.hashs[key] = value

    def get(self, key: int) -> int:
        if key in self.hashs:
            return self.hashs[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashs:
            del self.hashs[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)