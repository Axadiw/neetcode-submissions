class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        is_negative = x < 0
        x = abs(x)
        while x>0:
            digits.append(x%10)
            x = x // 10
        merged = ''.join([str(x) for x in digits])
        
        if merged == '' or float(merged) > math.pow(2,31)-1 or float(merged) < -math.pow(2,31):
            return 0
        return int(merged) * (-1 if is_negative else 1)
        