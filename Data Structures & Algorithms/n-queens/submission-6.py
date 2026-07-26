class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret_val = []
        seen = set()
        # def position(pos):
        #     return (pos // n, pos % n)

        def are_attacking(pos_a,pos_b):
            # pos_a = position(a)
            # pos_b = position(b)

            return pos_a[0] == pos_b[0] or pos_a[1] == pos_b[1] or abs(pos_a[0] - pos_b[0]) == abs(pos_a[1] - pos_b[1])

        def output_representation(positions):
            array = []

            for i in range(n):
                array.append(['.']*n)
            
            for pos in positions:
                array[pos[0]][pos[1]] = 'Q'
            
            return [''.join(line) for line in array]

        def helper(positions, y):
            if len(positions) >= n:
                representation = ','.join(sorted([f"{str(x[0])},{str(x[1])}" for x in positions]))
                if not representation in seen:
                    ret_val.append(positions)
                    seen.add(representation)
                return
            
            if y >= n: return

            xses = set()
            for pos in positions:
                xses.add(pos[0])

            for x in [a for a in range(n) if not a in xses]:                                        
                are = False
                for pos in positions:
                    if are_attacking(pos, (x,y)):
                        are = True
                        break
                
                if not are:
                    new_set = positions.copy()
                    new_set.add((x,y))
                    helper(new_set, y+1)

        helper(set(), 0)

        return [output_representation(v) for v in ret_val]

