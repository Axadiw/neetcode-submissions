class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height = len(grid[0])
        width = len(grid)
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        # print(f"height: {height} width: {width}")

        for x in range(height):
            for y in range(width):
                # print(f"x {x} y {y}")
                if grid[y][x] != 2147483647:
                    continue 

                queue = deque()
                visited = set()
                queue.append((x,y))
                visited.add((x,y))
                
                length = 0
                found = False
                while queue:
                    length += 1
                    for _ in range(len(queue)):
                        element = queue.popleft()                        

                        for n in neighbours:
                            nx = element[0] + n[0]
                            ny = element[1] + n[1]

                            if nx < 0 or ny < 0 or nx >= height or ny >= width or (nx,ny) in visited or grid[ny][nx] == -1:
                                continue                                                                

                            if grid[ny][nx] == 0:
                                grid[y][x] = length
                                found = True
                                # print(f"found path for {(x,y)} path ends with {(nx,ny)} length: {length}")
                                break
                            
                            # print(f"analyzing path for {(x,y)} possible path goes through {(nx,ny)} lenght {length}")
                            queue.append((nx,ny))
                            visited.add((nx,ny))
                            
                        
                    if found:
                        break
                


        