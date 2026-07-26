class Node:
    def __init__(self, n: List[int]):
        self.val = n
        self.repr = ','.join(n)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret_val = [[]]
        snums = sorted(nums)

        def repr(array: List[int]):
            return ','.join([str(x) for x in array])

        i = 0
        while i < len(snums):
            for num in snums:            
                new = []
                for val in ret_val:
                    for i in range(len(val)+1):
                        copy = val.copy()
                        copy.insert(i, num)
                        new.append(copy)
                ret_val = new
            
            i += 1
            while i < len(snums) and snums[i] == snums[i-1]:
                i += 1

        mapa = {}
        for val in ret_val:
            r = repr(val)
            if not r in mapa:
                mapa[r] = val
            repr(val)
        return [x[1] for x in mapa.items()]        