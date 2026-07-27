class Solution:
    def reverseBits(self, n: int) -> int:
        ret_val = 0
        for _ in range(32):
            digit = n & 1
            n = n >> 1
            ret_val = ret_val << 1
            ret_val = ret_val | digit
        return ret_val