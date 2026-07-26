class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret_val = set()
        curr = ""

        def add_brackets(positions, s):
            return f"{s[:positions[0]]}({s[positions[0]:positions[1]]}){s[positions[1]:]}"
        
        def remove_brackets(positions, s):
            return f"{s[:positions[0]]}{s[positions[0]+1:positions[1]+1]}{s[positions[1]+2:]}"       

        def helper(i):
            nonlocal curr
            if i > n-1:
                ret_val.add(curr)
                return
            
            positions = [(0,0)]

            index = 0
            opened = 0
            while index < len(curr):                
                opened += 1 if curr[index] == '(' else -1                

                if opened == 0:
                    positions.append((0,index+1))
                index += 1
            
            index = len(curr) - 1
            opened = 0
            while index >= 0:
                opened += 1 if curr[index] == ')' else -1

                if opened == 0:
                    positions.append((index+1,len(curr)))
                
                index -= 1
            
            for pos in positions:
                curr = add_brackets(pos, curr)
                helper(i+1)
                curr = remove_brackets(pos, curr)
                    
        helper(0)
        return list(ret_val)
        