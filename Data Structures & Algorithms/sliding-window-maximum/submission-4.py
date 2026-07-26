import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        window = collections.deque()
        maxes = []
        for right in range(0, len(nums)):        
            
            while len(window) > 0 and nums[window[-1]] < nums[right]:
                item = window.pop()
                # print(f"removed {item} from the window")
            window.append(right)
            # print(f"after adding {nums[right]} (index{right}) to window we have window = {window}")

            if window[0] <= right - k:
                item = window.popleft()
                # print(f"removed {item} from the window (window too big)")

            # print(f"after cleanup we have window = {window}")
            if right >= k-1:
                # print(f"adding {window[0]} to maxes array")
                maxes.append(nums[window[0]])
                        
        return maxes
        # [3,3,2,5]

        # [3,3,2,5 ,1,2,3]
        #    0 1 2 3  4 5 6

