class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])
        # print(f"height: {height}, width: {width}")
        ret_val = []

        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def bfs(x,y):
            queue = deque()
            visited = set()
            
            pacific = False
            atlantic = False

            if x == 0 or y == 0:
                pacific = True
            if x == width -1  or y == height -1:
                atlantic = True

            queue.append((x,y))
            visited.add((x,y))

            while queue:
                for _ in range(len(queue)):
                    element = queue.popleft()
                    # print(f"analyzing {element} as next element starting from {(x,y)}")

                    for n in neighbours:
                        nx = element[0] + n[0]
                        ny = element[1] + n[1]

                        if nx < 0 or ny < 0 or nx >= width or ny >= height or (nx,ny) in visited or heights[element[1]][element[0]] < heights[ny][nx]:
                            # print(f"skipping {(nx,ny)} as next element starting from {(x,y)}, visited: {visited}, heights[e0][e1]: {heights[element[1]][element[0]]}")
                            continue
                        
                        if nx == 0 or ny == 0:
                            # print(f"{(x,y)} reached pacific ending on {(nx,ny)}")
                            pacific = True
                        if nx == width -1  or ny == height -1:
                            # print(f"{(x,y)} reached atlantic ending on {(nx,ny)}")
                            atlantic = True
                        
                        queue.append((nx,ny))
                        visited.add((nx,ny))
                        
                        if pacific and atlantic:
                            # print(f"{(x,y)} reached both oceans")                                
                            break
                    
                    if pacific and atlantic:
                        break
                
                if pacific and atlantic:                        
                    break
            if pacific and atlantic:
                ret_val.append([y,x])

        for x in range(width):
            for y in range(height):
                bfs(x,y)
                

        return ret_val
                        

                            



        