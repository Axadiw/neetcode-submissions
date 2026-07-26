class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret_val = []
        ret_val_hashes = set()
        
        curr = []
        curr_sum = 0
        scandidates = sorted(candidates)

        def helper(i):
            nonlocal curr_sum
            nonlocal ret_val
        
            if curr_sum == target:
                c = curr.copy()
                repra = ','.join([str(s) for s in c])

                if not repra in ret_val_hashes:
                    ret_val.append(c)
                    ret_val_hashes.add(repra)
                return

            if i > len(scandidates)-1 or curr_sum > target:                
                return            

            curr.append(scandidates[i])
            curr_sum += scandidates[i]
            helper(i+1)
            curr.pop()
            curr_sum -= scandidates[i]

            # Skip duplicates to avoid exploring redundant paths
            next_i = i + 1
            while next_i < len(scandidates) and scandidates[next_i] == scandidates[i]:
                next_i += 1
            helper(next_i)

        helper(0)
        return ret_val