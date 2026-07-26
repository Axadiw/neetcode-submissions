class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid[0])
        width = len(grid)
        if height == 0 or width == 0:
            return -1
        print(f"height {height} width {width}")
        
        queue = deque()
        time = 0

        for x in range(width):
            for y in range(height):
                print(f"{x} {y}")
                if grid[x][y] == 2:
                    queue.append((x,y))
        
        # if len(queue) == 0:
        #     return 0

        neigh = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            anything_rotten = False
            for _ in range(len(queue)):
                element = queue.popleft()

                for n in neigh:
                    x = element[0] + n[0]
                    y = element[1] + n[1]

                    if x >= 0 and y >= 0 and x < width and y < height and grid[x][y] == 1:
                        # print(f"{x} {y} rotten at time {time}")
                        grid[x][y] = 2
                        queue.append((x,y))
                        anything_rotten = True
            if anything_rotten:
                time += 1
        
        for x in range(width):
            for y in range(height):
                if grid[x][y] == 1:
                    return -1
        return time

# 110
# 011
# 012       
            
                    
                    
