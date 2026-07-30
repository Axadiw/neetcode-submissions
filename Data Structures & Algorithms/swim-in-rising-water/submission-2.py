class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        heap = [(grid[0][0],(0,0))]
        shortest = {}

        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        while heap:
            w1, coords = heapq.heappop(heap)
            if coords == (height-1,width-1):
                return w1
            
            if coords in shortest:
                continue
            shortest[coords] = w1
            
            for neighbour in neighbours:
                new_coords = (coords[0]+neighbour[0],coords[1]+neighbour[1])

                if new_coords[0] < 0 or new_coords[1] < 0 or new_coords[0] >=  height or new_coords[1] >= width:
                    continue
                
                heapq.heappush(heap,(max(w1,grid[new_coords[0]][new_coords[1]]),new_coords))
            


        