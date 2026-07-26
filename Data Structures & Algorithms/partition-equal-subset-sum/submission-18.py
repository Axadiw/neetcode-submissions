class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nsum = 0
        for n in nums:
            nsum += n
        hsum = int(nsum/2)

        if nsum % 2 != 0:
            return False

        dp = [0] * (len(nums) + 1)
        for i in range(len(dp)):
            dp[i] = [True] + [False] * hsum

        
        for i in range(1, len(dp)):
            for j in range(1, hsum + 1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]] if nums[i-1] <= j else dp[i-1][j]
        
        # for i in dp:
        #     print(' '.join([str(x) for x in i]))
        
        return dp[-1][-1]