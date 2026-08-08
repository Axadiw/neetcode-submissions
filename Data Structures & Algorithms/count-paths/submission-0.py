class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0] * m for x in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    ways[i][j] = 1    
                    continue
                up = ways[i][j-1] if j-1>=0 else 0
                left = ways[i-1][j] if i-1>=0 else 0
                ways[i][j] = up + left
        
        print(ways)
        
        return ways[n-1][m-1]