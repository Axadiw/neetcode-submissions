class Solution:
    def trap(self, height: List[int]) -> int:
        return_value = 0

        max_lefts = [0]*len(height)
        max_rights = [0]*len(height)

        cur_max_left = 0    
        cur_max_right = 0    
        for i in range(1,len(height)-1):
            cur_max_left = max(cur_max_left, height[i-1])
            max_lefts[i] = cur_max_left
                
        for i in range(len(height)-2,-1,-1):
            cur_max_right = max(cur_max_right, height[i+1])
            max_rights[i] = cur_max_right

        print(f"max_lefts: {max_lefts}")
        print(f"max_rights: {max_rights}")
        for i in range(0,len(height)-1):
            return_value += max(min(max_lefts[i],max_rights[i]) - height[i],0)
                

        return return_value        
            

            






        