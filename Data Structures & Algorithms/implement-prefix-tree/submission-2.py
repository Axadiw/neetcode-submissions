class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        l = len(word)
        for index, s in enumerate(word):
            if s not in current.children:
                new_node = TrieNode()
                current.children[s] = new_node                
                current = new_node
            else:
                current = current.children[s]

            if index == l-1:
                current.isEnd = True


    def search(self, word: str) -> bool:
        current = self.root

        for s in word:
            if s in current.children:
                current = current.children[s]
            else:
                return False
        return current.isEnd

        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for s in prefix:
            if s in current.children:
                current = current.children[s]
            else:
                return False
        return True
        
        