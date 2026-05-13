import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # print(f'{r}')
        # mid = int((r - l) / 2)
        # print(f"{mid}")

        while l <= r:
            mid = int(l + math.floor((r - l) / 2))

            
            if target > nums[mid]:
                print(f"set l to {mid}, nums[{mid}] is {nums[mid]} (l={l} r={r})")
                l = mid +1
            elif target < nums[mid]:
                print(f"set r to {mid}, nums[{mid}] is {nums[mid]} (l={l} r={r})")
                r = mid -1
            else:
                return mid
  
                

        return -1