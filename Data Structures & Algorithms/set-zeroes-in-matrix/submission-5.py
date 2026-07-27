class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])
        
        def dfs(y,x,x_dir,y_dir):
            if x_dir == -1 and y_dir == 0:
                if x<0:
                    return
            elif x_dir == 0 and y_dir == -1:
                if y<0:
                    return
            elif x_dir == 1 and y_dir == 0:
                if x>=width:
                    return
            elif x_dir == 0 and y_dir == 1:        
                if y>=height:
                    return
            
            if matrix[y][x] != 0:
                matrix[y][x] = None
            dfs(y+y_dir,x+x_dir,x_dir,y_dir)

        for x in range(width):
            for y in range(height):
                if matrix[y][x] == 0:
                    dfs(y,x,-1,0)
                    dfs(y,x,1,0)
                    dfs(y,x,0,1)
                    dfs(y,x,0,-1)
        
        for x in range(width):
            for y in range(height):
                if matrix[y][x] == None:
                    matrix[y][x] = 0
        