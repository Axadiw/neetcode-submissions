class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        subset = []

        def helper(i, subset):
            if i > len(nums)-1:
                return_array.append(subset.copy())
                return

            subset.append(nums[i])
            helper(i+1, subset)
            subset.pop()
            helper(i+1, subset)

        helper(0,[])
        return return_array
        