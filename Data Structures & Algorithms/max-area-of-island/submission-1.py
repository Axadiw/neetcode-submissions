class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_of_islands = 0
        sizes_of_islands = [0]
        w = len(grid)
        h = len(grid[0])
        

        def dfs(x,y,visited,index):
            nonlocal grid
            if x<0 or y<0 or x>=w or y>=h or grid[x][y] != 1:
                return

            if not (x,y) in visited:
                visited.add((x,y))
                # print(f"=={index}==x:{x} y:{y}=")
                grid[x][y] = index
                dfs(x-1,y,visited,index)
                dfs(x+1,y,visited,index)
                dfs(x,y-1,visited,index)
                dfs(x,y+1,visited,index)
                sizes_of_islands[-index-1] += 1
                visited.remove((x,y))

        for y in range(h):
            for x in range(w):
                if grid[x][y] == 1:
                    num_of_islands += 1
                    sizes_of_islands.append(0)
                    dfs(x,y,set(),-num_of_islands)
        print(sizes_of_islands)
        return max(sizes_of_islands)