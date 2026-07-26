class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(selected_costs):
            selected_costs += [0]
            curr = [-1]*len(selected_costs)
            
            curr[0] = selected_costs[0]
            curr[1] = selected_costs[0] + selected_costs[1]

            i = 2
            while i<len(selected_costs):
                curr[i] = min(curr[i-1], curr[i-2]) + selected_costs[i]
                i+=1
            
            return curr[-1]
            

            
        
        return min(helper(cost), helper(cost[1:].copy()))
        