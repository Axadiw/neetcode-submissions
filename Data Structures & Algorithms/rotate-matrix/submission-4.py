class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [0] * n
        for i in range(n):
            new_matrix[i] = [0] * n
        
        def calculate(y,x):
            return (x,n-y-1)

        count = 0
        cur = (0,0)
        tmp = -1
        print(f"n= {n}")
        for y in range(math.ceil(n/2)):
            print(f"for y={y}")
            print(f"x range: {y} - {n-y-1}")
            for x in range(y,n-y-1):

                curr = [y,x]
                tmp = matrix[curr[0]][curr[1]]            
                print(f">>new start {curr}")
                for _ in range(4):
                    print('__')
                    print(f"prev {curr}")

                    curr = calculate(curr[0],curr[1])
                    tmp2 = matrix[curr[0]][curr[1]]            
                    matrix[curr[0]][curr[1]] = tmp
                    print(f"after {curr} ({tmp})")
                    tmp = tmp2

                    
                    print('__')


        # while count < n*n:
        #     new_index = calculate(cur[0],cur[1])
        #     tmp = matrix[new_index[0]][new_index[1]]            
        #     matrix[new_index[0]][new_index[1]] = matrix[cur[0]][cur[1]]
        #     print(f"{cur} -> {new_index}")
        #     cur = new_index

        #     count +=1
        
        