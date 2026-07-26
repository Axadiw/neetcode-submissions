class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret_val = []
        curr = []

        def helper(i):
            if i > len(nums)-1:
                ret_val.append(curr.copy())
                return
            
            for idx in range(len(curr)+1):
                curr.insert(idx,nums[i])
                helper(i+1)
                curr.pop(idx)
        
        helper(0)
        return ret_val