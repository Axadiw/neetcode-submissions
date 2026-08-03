class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]

        def rob(n):
            if len(n) == 0:
                return 0
            
            if len(n) == 1:
                return n[0]
            
            if len(n) == 2:
                return max(n[0], n[1])

            res = [0] * len(n)
            res[0] = n[0]
            res[1] = max(n[0],n[1])

            i = 2
            while i<len(n):
                res[i] = max(n[i]+res[i-2], res[i-1])
                i+=1
            return res[-1]
        
        return max(rob(nums[1:]), rob(nums[:-1]))
        