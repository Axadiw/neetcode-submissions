class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret_val = [[]]

        def subsets_2(nums: List[int], list_so_far:List[int]):
            nonlocal ret_val
            for idx,num in enumerate(nums):
                added_array = list_so_far + [num]
                # print(f"adding array {added_array}")
                ret_val.append(added_array)
                subsets_2(nums[idx+1:], added_array)
        
        subsets_2(nums,[])
        # print(ret_val)

        return ret_val
        