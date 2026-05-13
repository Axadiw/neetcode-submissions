class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while(i < len(numbers) and i >= 0):
            current_target = numbers[i] + numbers[j]
            if current_target == target:
                return [i+1, j+1]
            
            if current_target > target:
                j -= 1
            else:
                i += 1

        