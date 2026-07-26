class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nsum = 0
        for n in nums:
            nsum += n
        if nsum % 2 != 0:
            return False

        hsum = int(nsum/2)
        
        cache = [0] * len(nums)
        for i in range(len(cache)):
            cache[i] = [None] * (hsum+1)
        


        def helper(i, cur):            
            if cache[i][cur] != None:
                return cache[i][cur]

            if cur - nums[i] == 0:
                return True

            if i == len(nums) -1:
                return False          

            # print('befor')
            # for a in cache:
            #     print(' '.join([str(x) for x in a]))

            val = helper(i+1,cur) or helper(i+1,cur-nums[i])
            cache[i][cur] = val

            # print(f'after {val} {i} {cur}')
            # for a in cache:
            #     print(' '.join([str(x) for x in a]))
            return val
        
        v = helper(0,hsum)

        return v