class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(n):
            count = 0
            while n>0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count
        
        ret_val = []
        for i in range(n+1):
            ret_val.append(count_ones(i))
        return ret_val
        