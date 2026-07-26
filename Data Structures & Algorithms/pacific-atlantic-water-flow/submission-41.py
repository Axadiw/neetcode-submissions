class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])
        # print(f"height: {height}, width: {width}")
        ret_val = set()

        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]        

        def bfs(x,y, success):
            queue = deque()
            visited = set()
            
            queue.append((x,y))
            visited.add((x,y))
            success((y,x))                

            while queue:
                for _ in range(len(queue)):
                    element = queue.popleft()
                    # print(f"analyzing {element} as next element starting from {(x,y)}")

                    for n in neighbours:
                        nx = element[0] + n[0]
                        ny = element[1] + n[1]

                        if nx < 0 or ny < 0 or nx >= width or ny >= height or (nx,ny) in visited or heights[element[1]][element[0]] > heights[ny][nx]:                            
                            # print(f"skipping {(nx,ny)} as next element starting from {(x,y)}, visited: {visited}, heights[e0][e1]: {heights[element[1]][element[0]]}")
                            continue
                        
                        # print(f"adding {(x,y)}")
                        success((ny,nx))                
                        
                        queue.append((nx,ny))
                        visited.add((nx,ny))                                              

        myset = set()
        def add_to_set(val):
            myset.add(val)
        
        def check_set(val):
            if val in myset:
                ret_val.add(val)

        for x in range(width):
            # print(f"==PACIFIC TOP {(x,0)}==")
            bfs(x,0, add_to_set)
        
        for y in range(height):
            # print(f"==PACIFIC EFT {(0,y)}==")
            bfs(0,y, add_to_set)            
        # print(myset)
        for x in range(width):
            bfs(x,height-1, check_set)
        for y in range(height):
            bfs(width-1,y, check_set)            
                                
        return list(ret_val)
                        

                            



        