class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        returnArray = [1]*len(nums)

        if len(nums) <= 1:
            return nums

        for i in range(0,len(nums)):
            if i > 0:
                returnArray[i] = prefix    
            prefix *= nums[i]
            print(f'tablica wynikowa {returnArray} prefix to {prefix}')

        for i in range(len(nums)-1,-1,-1):
            
            if i < len(nums):
                returnArray[i] *= suffix    
            suffix *= nums[i]
            print(f'tablica wynikowa {returnArray} przemnazalem przez {suffix}')
        
        return returnArray
        
        