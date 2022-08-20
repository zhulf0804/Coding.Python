class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur[-1] = True 

    def search(self, word):
        cur = self.root
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        if -1 in cur:
            return True
        return False

    def startsWith(self, prefix):
        cur = self.root
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
