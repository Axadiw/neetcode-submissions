class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret_val = []
        curr = []
        snums = sorted(nums)

        def currsum():
            acc = 0
            for item in curr:
                acc += item
            return acc

        def helper(i, cur_sum):
            # aSum = currsum()                
            # print(f"sum of {curr} is {aSum}")
            
            if cur_sum == target:
                ret_val.append(curr.copy())
                return
            # print(f"{i} curr:{curr}")
            if i>len(nums)-1:        
                # print(f"i>len(nums)-1. i{i}, len: {len(nums)-1}")        
                return

            if cur_sum > target:
                return
            
            # for j in range(0,len(nums)):
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
        