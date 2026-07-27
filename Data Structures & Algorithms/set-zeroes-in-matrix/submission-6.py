class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        width = len(matrix)
        height = len(matrix[0])

        zeros = []
        for i in range(width):
            for j in range(height):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        
        for zero in zeros:
            for i in range(width):
                matrix[i][zero[1]] = 0

            for j in range(height):
                matrix[zero[0]][j] = 0

        