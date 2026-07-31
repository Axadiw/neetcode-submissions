class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix)
        height = len(matrix[0])
        # 0 - right
        # 1 - down
        # 2 - left
        # 3 - up

        visited = set()
        ret_val = []
        direction = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        curr = (0,0)

        while len(visited) < width*height :
            ret_val.append(matrix[curr[0]][curr[1]])
            visited.add(curr)
            next_curr = (curr[0]+directions[direction][0],curr[1]+directions[direction][1])
            if next_curr[0] < 0 or next_curr[1] < 0 or next_curr[0] >= width or next_curr[1] >= height or next_curr in visited:
                direction = (direction + 1)%4
                next_curr = (curr[0]+directions[direction][0],curr[1]+directions[direction][1])
            curr = next_curr

        
        return ret_val