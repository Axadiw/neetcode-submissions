class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        sorted_index = 0
        if nums[right] < nums[left]:
            while right - left > 1:
                mid = (right - left)//2 + left
                print(f"left{left} right {right} mid {mid}")
                
                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid
            
            print(f"end left {left} right {right}")
            sorted_index = left if nums[left] < nums[right] else right
        print(f"sorted_index {sorted_index}")
        sorted_array = nums[sorted_index:] + nums[:sorted_index]
        print(f"sorted_array {sorted_array}")

        left = 0
        right = len(sorted_array) - 1

        while left <= right:
            mid = (right - left)//2 + left
            print(f"left{left} right {right} mid {mid}")

            if sorted_array[mid] > target:
                right = mid - 1
            elif sorted_array[mid] < target:
                left = mid + 1
            else:
                return (mid + sorted_index) % len(sorted_array)
        
        print(f"end left{left} right {right}")
        return -1