class TrieNode:
    def __init__(self, value: string, isEnd:bool):
        self.value = value
        self.children = {}
        self.isEnd = isEnd

class Trie:
    def __init__(self):
        self.root = TrieNode(value='',isEnd=False)
        self.cache = {}
        self.maxSize = 0
    
    def add(self, word):
        curr = self.root
        for s in word:
                        
            if not s in curr.children:
                newNode = TrieNode(value=s, isEnd=False)
                curr.children[s] = newNode            
            curr = curr.children[s]
        
        curr.isEnd = True
        self.cache = {}
        self.maxSize = max(self.maxSize, len(word))
    
    def isPrefix(self, word):
        if len(word) > self.maxSize:
            return (False, False)
        
        print(f"checking for prefix {word}")
        if word in self.cache:
            return self.cache[word]

        curr = self.root

        for s in word:
            if s in curr.children:
                curr = curr.children[s]
            else:
                self.cache[word] = (False,False)
                return self.cache[word]
        
        self.cache[word] = (True,curr.isEnd)
        return self.cache[word]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        
        potentialLs = set([0])
        lastL = None
        R = 1

        while R <= len(s):
            foundPrefix = False
            for L in list(potentialLs): 
                isPrefix = trie.isPrefix(s[L:R])

                if isPrefix[0]:                    
                    foundPrefix = True
                else:
                    continue
                
                if isPrefix[1]:
                    potentialLs.add(R)
                    lastL = R
                
            if not foundPrefix:
                return False
            R+=1
        print(potentialLs)
        return lastL==len(s)

        