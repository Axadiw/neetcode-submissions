class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        ret_val = 0
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]

        cache = {}
        def dfs(y,x):            
            if (y,x) in cache:
                return cache[(y,x)]
            maxes = 1
            for neighbour in neighbours:
                new_y = y + neighbour[1]
                new_x = x + neighbour[0]
                # print(f"{new_y} {new_x}")
                if new_y>=0 and new_x>=0 and new_x < width and new_y<height and matrix[new_y][new_x] > matrix[y][x]:
                    maxes = max(maxes, 1 + dfs(new_y,new_x))
            cache[(y,x)] = maxes
            return maxes



        for y in range(height):
            for x in range(width):
                ret_val = max(ret_val, dfs(y,x))
        
        return ret_val
        