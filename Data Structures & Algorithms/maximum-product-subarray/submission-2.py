class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        def helper(n):
            # print(f"execute for {n}")
            ret = [(0,0)] * len(n)
            ret[0] = (n[0], n[0])
            for i in range(1,len(n)):
                now_times_prev = ret[i-1][0]*n[i]
                if n[i] == 0:
                    ret[i] = (1,ret[i-1][1])
                else:
                    ret[i] = (now_times_prev, max(now_times_prev, ret[i-1][1]))
            # print(f"for {n} ret is {ret}")
            return ret[-1][1]
        
        r = -sys.maxsize
        for i in range(len(nums)):
            r = max(r, helper(nums[i:]))
        return r
