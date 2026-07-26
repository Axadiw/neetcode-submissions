class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        w = len(grid)
        h = len(grid[0])
        print(f"h: {h}")
        print(f"w: {w}")


        def dfs(x,y,visited,index):
            nonlocal grid
            if x<0 or y<0 or x>=w or y>=h or grid[x][y] != "1":
                return

            if not (x,y) in visited:
                visited.add((x,y))
                print(f"=={index}==x:{x} y:{y}=")
                grid[x][y] = index
                dfs(x-1,y,visited,index)
                dfs(x+1,y,visited,index)
                dfs(x,y-1,visited,index)
                dfs(x,y+1,visited,index)
                visited.remove((x,y))

        for y in range(h):
            for x in range(w):
                print(f"x:{x} y:{y} color:{grid[x][y]}")
                if grid[x][y] == "1":
                    num_of_islands += 1
                    dfs(x,y,set(),-num_of_islands)
        return num_of_islands

        