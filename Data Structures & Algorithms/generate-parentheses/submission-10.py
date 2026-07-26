class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret_val = []
        curr = []


        def helper(i,opened,closed):
            if opened == closed and closed == n and len(curr) > 0:
                ret_val.append(''.join(curr.copy()))

            
            if opened < n:
                curr.append('(')
                helper(i+1, opened+1, closed)
                curr.pop()
            
            if closed < opened:
                curr.append(')')
                helper(i+1, opened, closed+1)
                curr.pop()


        helper(0,0,0)
        print(ret_val)
        return ret_val
        