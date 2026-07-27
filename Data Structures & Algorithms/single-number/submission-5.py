class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        wat = nums[0]

        for i in range(1,len(nums)):
            wat = wat ^ nums[i]
        
        return wat
        