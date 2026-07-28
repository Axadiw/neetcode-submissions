class Solution:
    def getSum(self, a: int, b: int) -> int:
        acc = 0
        res = 0
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        # Standardize negative numbers to 32-bit unsigned representation
        a &= MASK
        b &= MASK
        for i in range(32):
            digit = 0
            if (a >> i) & 1 > 0 and (b >> i) & 1 > 0:
                if acc == 1:
                    digit = 1
                else:
                    digit = 0
                    acc = 1
            else:
                digit = ((a >> i) & 1) | ((b >> i) & 1)
                if digit == 1:
                    if acc == 1:
                        digit = 0
                        acc = 1
                else:
                    if acc == 1:
                        digit = 1
                        acc = 0

            res = (res | (digit << i)) & MASK
        
        # Convert back to Python's arbitrary precision signed integer
        return res if res <= MAX_INT else ~(res ^ MASK)

