class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        width = len(board)
        height = len(board[0])

        def helper(x,y,prefix, seen):
            
            if (x,y) in seen:
                # print(f"finishing eariler {prefix} (already seen {(x,y)})")
                return False
            
            if len(prefix)>len(word):
                # print(f"finishing eariler {prefix}, too long prefix: {len(prefix)}>{len(word)}")
                return False

            if word[:len(prefix)] != prefix:
                # print(f"{word[:len(prefix)]} != {prefix}")
                return False
                
            # print(f"visiting {x},{y} prefix:{prefix}")

            if prefix == word:
                found = True
                return True
            
            seen.add((x,y))
            # letter = 
            found = False
            if x + 1 < width and helper(x+1,y,prefix+board[x+1][y],seen.copy()):
                return True

            if y + 1 < height and helper(x,y+1,prefix+board[x][y+1],seen.copy()):
                return True    

            if y - 1 >= 0 and helper(x,y-1,prefix+board[x][y-1],seen.copy()):
                return True        

            if x - 1 >= 0 and helper(x-1,y,prefix+board[x-1][y],seen.copy()):
                return True     
            
            return False


        for x, line in enumerate(board):
            for y, letter in enumerate(line):
                if helper(x,y,board[x][y],set()):
                    return True

        return False