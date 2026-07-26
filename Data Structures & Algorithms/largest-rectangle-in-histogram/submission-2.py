class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for idx, h in enumerate(heights):
            # find left
            left = idx
            right = idx
            while left > 0:
                left -= 1
                if heights[left] < h:
                    left += 1
                    break
            
            while right < len(heights)-1:
                right += 1
                if right < len(heights) and heights[right] < h:
                    right -= 1
                    break                
            print(f"for index={idx} with height={h} left={left} right={right}")
            area = max(area, (right-left+1)*h)
                
        
        return area