class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0

            curr += n
            max_sum = max(max_sum, curr)
        
        return max_sum
                
        