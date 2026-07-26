class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
                return 0
            
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])

        i = 0
        sterted_from_prev_prev = False
        end = 2
        while i<len(nums)-2:
            if i == 0:
                prevprev = nums[-2]
                prev = nums[-1]
                sterted_from_prev_prev = nums[i]+prevprev > prev
            elif i == 1:
                prevprev = nums[-1]
                prev = res[0]
            else:
                prevprev = res[i-2]
                prev = res[i-1]
            
            print(f"for {i} nums[i]+prevprev is {nums[i]+prevprev}, prev is {prev}, prevprev is {prevprev}")
            res[i] = max(nums[i]+prevprev, prev)
            i+=1
        print(res)
        
        print('-')
        ret = res[-4] if sterted_from_prev_prev else res[-3]
        if sterted_from_prev_prev:
                        
            res = [0] * len(nums)
            res[0] = nums[0]
            res[1] = max(nums[0],nums[1])

            i = 0
            end = 2
            while i<len(nums)-2:
                if i == 1:
                    prevprev = nums[-1]
                    prev = res[0]
                else:
                    prevprev = res[i-2]
                    prev = res[i-1]
                
                print(f"for {i} nums[i]+prevprev is {nums[i]+prevprev}, prev is {prev}, prevprev is {prevprev}")
                if i == 0:
                    res[i] = max(nums[-1],nums[0])
                else:
                    res[i] = max(nums[i]+prevprev, prev)
                i+=1
            print(res)
            ret = max(ret, res[-3])

        
        return ret
        