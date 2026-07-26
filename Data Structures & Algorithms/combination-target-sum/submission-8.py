class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret_val = []
        curr = []
        snums = nums #sorted(nums)

        def helper(i, cur_sum):
            
            if cur_sum == target:
                ret_val.append(curr.copy())
                return

            if i>len(nums)-1:        
                return

            if cur_sum > target:
                return
            
            curr.append(snums[i])
            helper(i,cur_sum + snums[i])
            helper(i+1, cur_sum + snums[i])
            curr.pop()    

            helper(i+1, cur_sum)
            




        helper(0,0)

        seen = {}
        a = []
        for item in ret_val:
            repr = ','.join([str(x) for x in sorted(item)])
            if not repr in seen:
                seen[repr] = True
                a.append(item)

        return a
        