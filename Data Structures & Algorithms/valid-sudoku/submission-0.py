import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        squares = []

        for i in range(0,9):
            rows.append(set())
            cols.append(set())
            squares.append(set())

        for r, row in enumerate(board):
            for i, item in enumerate(row):
                if item == '.':
                    continue


                if item in rows[r]:
                    print(f'Zjebalo sie na row {r}, probowalem dodac {item} do {rows[r]}')
                    return False
                
                print(f'rows: {rows}')
                rows[r].add(item)

                if item in cols[i]:
                    print(f'Zjebalo sie na cols {i}, probowalem dodac {item} do {cols[i]}')
                    return False
                
                cols[i].add(item)

                squareId = math.floor(r/3) + 3*math.floor(i/3)

                if item in squares[squareId]:
                    print(f'Zjebalo sie na square {squareId} row {r} col {i}, probowalem dodac {item} do {squares[squareId]}')
                    return False
                
                squares[squareId].add(item)


        return True
        