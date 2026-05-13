class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for id1, num in enumerate(nums):
            for id2, num2 in enumerate(nums):
                if num == num2 and id1 != id2:
                    return True
        
        return False