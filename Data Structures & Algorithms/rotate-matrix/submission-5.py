class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [0] * n
        for i in range(n):
            new_matrix[i] = [0] * n
        
        def calculate(y,x):
            return (x,n-y-1)

        cur = (0,0)
        tmp = -1
        for y in range(math.ceil(n/2)):
            for x in range(y,n-y-1):

                curr = [y,x]
                tmp = matrix[curr[0]][curr[1]]            
                for _ in range(4):
                    curr = [curr[1],n-curr[0]-1]
                    tmp2 = matrix[curr[0]][curr[1]]            
                    matrix[curr[0]][curr[1]] = tmp
                    tmp = tmp2
