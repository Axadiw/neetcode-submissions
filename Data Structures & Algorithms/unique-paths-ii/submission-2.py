class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        paths = [[0] * width for _ in range(height)]

        for y in range(height):
            for x in range(width):
                if x==0 and y==0:
                    paths[y][x] = 1- obstacleGrid[0][0]
                    continue
            
                up = paths[y-1][x] if y-1 >= 0 else 0
                left = paths[y][x-1] if x-1 >= 0 else 0
                print(f"for x={x} and y={y} initial up={up} left={left}")
                if up > 0 and obstacleGrid[y-1][x] > 0:
                    print(f"obstacle found, zeroing up")
                    up = 0
                if left > 0 and obstacleGrid[y][x-1] > 0:
                    print(f"obstacle found, zeroing left")
                    left = 0

                paths[y][x] = up + left
        print(paths)
        return paths[height-1][width-1]