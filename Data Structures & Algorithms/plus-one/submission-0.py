class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        acc = 1
        
        for i in range(len(digits)-1,-1,-1):
            tmp_sum = digits[i] + acc
            digits[i] = tmp_sum % 10
            acc = tmp_sum // 10
            print(f"for {i} acc is {acc}")
        return ([acc] if acc > 0 else []) + digits
            
            
        