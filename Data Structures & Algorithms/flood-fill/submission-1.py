class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        width = len(image)
        height = len(image[0])
        def dfs(x,y,visited):
            if x < 0 or y < 0 or x >= width or y >= height:
                return
            # print(f"visiting {x} {y} it has color {image[x][y]}")
            
            if image[x][y] == start_color and not (x,y) in visited:
                visited.add((x,y))
                image[x][y] = color
                dfs(x-1,y, visited)
                dfs(x+1,y, visited)
                dfs(x,y-1, visited)
                dfs(x,y+1, visited)
                visited.remove((x,y))            

        dfs(sr,sc,set())
        return image
        