class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        l = len(word)
        for index, letter in enumerate(word):
            if not (letter in curr.children):
                new_node = TrieNode()
                curr.children[letter] = new_node
                curr = new_node
            else:
                curr = curr.children[letter]
            
            if index == l - 1:
                curr.isEnd = True


        

    def search(self, word: str) -> bool:
        def search_rec(word: str, root_node: TrieNode) -> bool:
            curr = root_node    
            for index, s in enumerate(word):
                if s == '.':
                    for node in curr.children.values():
                        if search_rec(word[index+1:], node):
                            return True
                    return False

                elif s in curr.children:
                    curr = curr.children[s]
                else:
                    return False
        
            return curr.isEnd
        
        return search_rec(word,self.root)

        
