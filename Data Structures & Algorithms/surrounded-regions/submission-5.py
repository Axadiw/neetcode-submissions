class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])

        def dfs(y,x, visited):
            # print(f"analyzing {(y,x)} visited: {visited}")
            if board[y][x] == 'O' and (x == 0 or y == 0 or x == width-1 or y == height-1):
                # print(f"{(y,x)} would return -1")
                return -1
            
            if (y,x) in visited or board[y][x] == 'X':
                # print(f"{(y,x)} would return empty array")
                return []
            
            visited.add((y,x))
            left = dfs(y,x-1,visited)
            if left == -1:
                return -1
            right = dfs(y,x+1,visited)
            if right == -1:
                return -1
            up = dfs(y-1,x,visited)
            if up == -1:
                return -1
            down = dfs(y+1,x,visited)
            if down == -1:
                return -1
            # print(f"{(y,x)}: left {left} right: {right} up {up} down {down} visited: {visited}")
            return left + right + up + down + [(y,x)]
            

        for x in range(width):
            for y in range(height):
                # print(f"== Starting analysis for {(y,x)}  ==")
                elements = dfs(y,x,set())
                # print(f"for {(y,x)} ({board[y][x]})found elements {elements}")
                if elements != -1:
                    
                    for element in elements:
                        board[element[0]][element[1]] = 'X'

        