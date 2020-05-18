class Node:
    def __init__(self):

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c]

    def search(self, word: str) -> bool:

    def startsWith(self, prefix: str) -> bool:



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
