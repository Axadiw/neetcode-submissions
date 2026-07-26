class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]
        
        if len(nums) == 1:
            return nums[0]

        while right - left > 1:
            mid = (right - left) // 2 + left
            num = nums[mid]
            # print(f"left {left} right {right} mid {mid} num {num}")

            if num > nums[0]:
                # print(f"num > nums[0]")
                left = mid + 1
            #elif num < nums[0]:
            else:                
                # print('right = mid')
                right = mid
        
        return min(nums[left],nums[right])
        