class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        jumps = 0
        going_forward = True
        last_obstacle = -1
        while i < n-1:
            jumps += 1
            
            max_far = i + nums[i]
            # print(f"i = {i} max_far: {max_far}")
            found_better = False
            if max_far < n-1:
                # print(f'jump not enogh, looking for better rejump')
                for j in range(i,max_far+1):
                    if j + nums[j] > max_far:
                        # print(f"nice, I could reach {j+nums[j]} if ill stop on {j}")
                        found_better = True
                        max_far = j + nums[j]
                        i=j
            if not found_better:
                i = max_far


        return jumps
        