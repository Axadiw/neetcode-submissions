class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        curr = self.root

        for s in word:
            if not s in curr.children:
                new_node = TrieNode()
                curr.children[s] = new_node
            curr = curr.children[s]
        
        curr.isEnd = True
    
    def isPrefix(self, prefix: str) -> Tuple[bool,bool]:
        curr = self.root

        for s in prefix:
            if not s in curr.children:
                return False, False
            curr = curr.children[s]

        # isprefix, isend
        return True, curr.isEnd

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        width = len(board)
        if width == 0:
            return []
        height = len(board[0])

        tree = PrefixTree()
        for word in words:
            tree.insert(word)

        found_words = set()
        def start_finding(i,j,prefix,indexes):
            # print(f"i:{i} j:{j} prefix:{prefix} indexes:{indexes}")
            if i > width or j > height:
                return
            letter = board[i][j]
            new_word = prefix+letter
            is_prefix, is_end = tree.isPrefix(new_word)

            if is_end:
                found_words.add(new_word)
            if not is_prefix:
                return
            
            #up
            curr_index_repr = f"{i},{j}"
            index_repr = f"{i-1},{j}"
            if i-1 >= 0 and not index_repr in indexes:
                start_finding(i-1,j,new_word,indexes+[curr_index_repr])

            #down
            index_repr = f"{i+1},{j}"
            if i+1 < width and not index_repr in indexes:
                start_finding(i+1,j,new_word,indexes+[curr_index_repr])

            #left
            index_repr = f"{i},{j-1}"
            if j-1 >= 0 and not index_repr in indexes:
                start_finding(i,j-1,new_word,indexes+[curr_index_repr])

            #right
            index_repr = f"{i},{j+1}"
            if j+1 < height and not index_repr in indexes:
                start_finding(i,j+1,new_word,indexes+[curr_index_repr])

        for i in range(0,width):
            for j in range(0,height):
                start_finding(i,j,'',[])
        
        return list(found_words)
        