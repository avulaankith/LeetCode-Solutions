class Node:
    def __init__(self) -> None:
        self.children = {}
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.flag = True

    def search(self, word: str) -> bool:
        # node = self.root

        def dfs(idx, root):
            node = root
            for i in range(idx,len(word)):
                if word[i] == ".":
                    for child in node.children:
                        if dfs(i+1, node.children[child]):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.flag
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)