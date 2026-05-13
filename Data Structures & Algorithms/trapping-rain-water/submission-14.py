class Solution:
    def trap(self, height: List[int]) -> int:
        return_value = 0

        

        left,right = 0,len(height)-1
        max_left, max_right = height[left],height[right]

        while left < right:
            if height[left] < height[right]:                
                left += 1
                max_left = max(max_left, height[left])
                
                print(f"L{left} adding {max(0,min(max_left, max_right) - height[left])} left {left} right {right} max_left {max_left} max_right {max_right}")
                return_value += max(0,min(max_left, max_right) - height[left])
            else:                
                right -= 1
                max_right = max(max_right, height[right])
                
                print(f"R{right} adding {max(0,min(max_left, max_right) - height[right])} left {left} right {right} max_left {max_left} max_right {max_right}")
                return_value += max(0,(min(max_left, max_right) - height[right]))
                

        return return_value   
            

            






        