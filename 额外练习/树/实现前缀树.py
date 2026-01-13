class Trie:

    def __init__(self):
        self.trie = {}
    def insert(self, word: str) -> None:
        tree = self.trie
        for i in word:
            if i in tree.keys():
                tree = tree[i]
            else:
                tree[i] = {}
                tree = tree[i]
        else:
            tree['Y'] = 1
    def search(self, word: str) -> bool:
        tree = self.trie
        for i in word:
            if i in tree.keys():
                tree = tree[i]
            else:
                return False
        else:
            if 'Y' in tree.keys():
                return True
        return False
    def startsWith(self, prefix: str) -> bool:
        tree = self.trie
        for i in prefix:
            if i in tree.keys():
                tree = tree[i]
            else:
                return False
        else:
            if len(tree.keys()) != 0:
                return True
        return False