class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def helper(i):
            if i in cache:
                return cache[i]
            if i == len(nums)-1:
                return 0
            
            max_val = 0
            for j in range(i+1, len(nums)):
                # print(f'j is {j}')
                if nums[j] > nums[i]:
                    # print(f"cheking helper for {j}")
                    max_val = max(helper(j)+1, max_val)
            
            cache[i] = max_val
            return max_val

        max_val = -1
        for i in range(len(nums)-1,-1,-1):            
            max_val = max(max_val, helper(i))
        return max_val +1
        