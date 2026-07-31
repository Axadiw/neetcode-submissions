class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        # 0 - right
        # 1 - down
        # 2 - left
        # 3 - up

        visited = set()
        ret_val = []
        direction = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        curr = (0,0)
        max_x = width
        min_x = 0
        max_y = height
        min_y = 0

        counter = 0
        while counter<width*height:
            ret_val.append(matrix[curr[0]][curr[1]])
            next_curr = (curr[0]+directions[direction][0],curr[1]+directions[direction][1])
            if next_curr[1] < min_x or next_curr[0] < min_y or next_curr[1] >= max_x or next_curr[0] >= max_y:
                if direction == 0 and curr[0] > 0: #right
                    min_y += 1

                if direction == 1: #down                   
                    max_x -= 1
                    if next_curr[0] == height:
                        min_y += 1
                
                if direction == 2: #left
                    max_y -= 1
                
                if direction == 3: #up
                    min_x += 1
                    
                direction = (direction + 1)%4
                # print(f"changed direction to {direction}. 0-right, 1-down, 2-left, 3-up")
                next_curr = (curr[0]+directions[direction][0],curr[1]+directions[direction][1])
            curr = next_curr
            counter += 1
        # print(f"min_x: {min_x} min_y: {min_y} max_x: {max_x} max_y: {max_y}")
        return ret_val