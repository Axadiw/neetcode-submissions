class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        
        reversing = False
        last_obstacle = -1
        while i < n-1:
            print(f"analyzing {i}")
            if i == -1:
                return False
            
            if not reversing:
                if nums[i] > 0:
                    i+=1                    
                else:
                    last_obstacle = i
                    reversing = True
                    i-=1
            else:
                if nums[i] + i > last_obstacle:
                    i = nums[i] + i
                    reversing = False
                else:
                    i-=1



        return True
        