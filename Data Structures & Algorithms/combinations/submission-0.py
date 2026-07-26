class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret_array = []
        curr = []

        def helper(i):
            if len(curr) == k:
                print(f'lencurr == k')
                ret_array.append(curr.copy())
                return
            if i > n:
                print(f'i > n')
                return
            
            curr.append(i)
            print(i)
            helper(i+1)
            curr.pop()

            helper(i+1)
            # for j in range(i,n+1):
            #     helper(j)
            
        
        helper(1)
        return ret_array
        