class Solution:

    def area(self, heights, left, right):
        print(f"{left}{right}")
        return min(heights[left],heights[right]) * abs(left-right)


    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        returnVal = 0

        while i<j:
            curArea = self.area(heights,i,j)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i+=1


            returnVal = max(returnVal, curArea)

        return returnVal

