class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret_array = []
        curr = []

        def helper(i):
            if len(curr) == k:
                ret_array.append(curr.copy())
                return
            if i > n:
                return
                
            for j in range(i,n+1):
                curr.append(j)
                helper(j+1)
                curr.pop()
            
        
        helper(1)
        return ret_array
        