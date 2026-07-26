class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 

        window = []
        maxes = []
        for right in range(0, len(nums)):
            window.append(nums[right])
            if len(window) > k:
                window.pop(0)
            
            if len(window) == k:
                maximum_value = -1
                for candidate in window:
                    maximum_value = max(maximum_value, candidate)
                maxes.append(maximum_value)
        return maxes

        