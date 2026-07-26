class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        return_array = []
        subset = []

        def helper(i, subset):
            if i > len(snums)-1:
                return_array.append(subset.copy())
                return

            subset.append(snums[i])
            helper(i+1, subset)
            subset.pop()

            cur = i + 1
            if len(nums) > 1:
                while cur <= len(snums)-1 and snums[cur] == snums[cur-1]:
                    cur += 1
            helper(cur, subset)

        helper(0,[])
        return return_array