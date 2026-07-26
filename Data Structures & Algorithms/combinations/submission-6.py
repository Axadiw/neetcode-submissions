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
            
            curr.append(i)
            helper(i+1)
            curr.pop()

            helper(i+1)            
        
        helper(1)
        return ret_array
        