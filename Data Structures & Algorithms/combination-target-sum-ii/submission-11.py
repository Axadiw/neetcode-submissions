class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret_val = []
        
        curr = []
        curr_sum = 0
        scandidates = sorted(candidates)

        def helper(i):
            nonlocal curr_sum
            nonlocal ret_val
        
            if curr_sum == target:
                ret_val.append(curr.copy())
                return

            if i > len(scandidates)-1 or curr_sum > target:                
                return            
            curr.append(scandidates[i])
            curr_sum += scandidates[i]
            helper(i+1)
            curr.pop()
            curr_sum -= scandidates[i]

            i += 1
            while i < len(scandidates) and scandidates[i] == scandidates[i-1]:
                i+=1
            helper(i)

        helper(0)

        return ret_val