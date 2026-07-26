class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        height = len(grid)
        
        width = len(grid[0])
        if height == 0 or width == 0 or grid[0][0] == 1:
            return -1

        queue.append((0,0))
        visited.add((0,0))

        found = False
        length = 0

        while queue:
            length += 1
            for _ in range(len(queue)):
                element = queue.popleft()
                if element == (width -1,height-1):
                    return length
                core_x = element[0]
                core_y = element[1]

                neibourghs = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
                for neibourgh in neibourghs:
                    x = core_x + neibourgh[0]
                    y = core_y + neibourgh[1]

                    if (x,y) in visited or x < 0 or y < 0 or x >= width or y >= height or grid[x][y] == 1:
                        continue
                    
                    queue.append((x,y))
                    visited.add((x,y))
        
        return -1

                
        