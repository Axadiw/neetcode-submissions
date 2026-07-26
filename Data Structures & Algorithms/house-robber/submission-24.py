class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        cache = {}
        def helper(i,n):
            if i == 0:
                return n[i]

            if i == 1:
                return max(n[0],n[1])
            
            if i in cache:
                return cache[i]

            cache[i] = max(helper(i-1,n), helper(i-2,n)+n[i])
            return cache[i]
        
        return helper(len(nums)-1,nums)
        # normal = helper(len(nums)-1,nums)
        # nums.reverse()
        # cache = {}
        # rev = helper(len(nums)-1, nums)
        # return max(normal,rev)
        