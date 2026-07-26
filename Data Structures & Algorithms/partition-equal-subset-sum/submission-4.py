class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nsum = 0
        for n in nums:
            nsum += n
        hsum = nsum/2
        
        cache = {}
        def helper(i, cur):
            repr = f"{i},{cur}"            
            if repr in cache:
                return cache[repr]
            if cur - nums[i] == 0:
                return True

            if i == len(nums) -1:
                return False          

            val = helper(i+1,cur) or helper(i+1,cur-nums[i])
            cache[repr] = val
            return val
        
        val = helper(0,hsum)
        print(cache)
        return val

    def canPartition2(self, nums: List[int]) -> bool:
        nsum = 0
        for n in nums:
            nsum += n
        hsum = nsum/2
        
        cache = {}
        def helper(i, cur):
            repr = f"{i},{cur}"            
            if repr in cache:
                return cache[repr]
            if cur + nums[i] == hsum:
                return True

            if i == len(nums) -1:
                return False          

            val = helper(i+1,cur) or helper(i+1,cur+nums[i])
            cache[repr] = val
            return val
        
        val = helper(0,0)
        print(cache)
        return val
        