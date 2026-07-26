class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret_val = [[]]

        for num in nums:            
            new = []
            for val in ret_val:
                for i in range(len(val)+1):
                    copy = val.copy()
                    copy.insert(i, num)
                    new.append(copy)
            ret_val = new

        return ret_val
        