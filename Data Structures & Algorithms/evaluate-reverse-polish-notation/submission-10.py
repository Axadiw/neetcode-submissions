import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        
        for t in tokens:
            print(f"token: {t}")
            if t == '+':
                tmp = stack.pop()
                tmp2 = stack.pop()
                result = tmp + tmp2
                stack.append(result)
                print(f"{tmp}+{tmp2} = {result}")
            elif t == '-':
                tmp = stack.pop()
                tmp2 = stack.pop()
                result = tmp2 - tmp
                stack.append(result)
                print(f"{tmp2}-{tmp} = {result}")
            elif t == '*':
                tmp = stack.pop()
                tmp2 = stack.pop()
                result = tmp * tmp2
                stack.append(result)
                print(f"{tmp}*{tmp2} = {result}")

            elif t == '/':
                tmp = stack.pop()
                tmp2 = stack.pop()
                tmp_res = tmp2 / tmp
                result = math.floor(tmp_res) if tmp_res > 0 else math.ceil(tmp_res)
                stack.append(result)            
                print(f"{tmp2}/{tmp} = {result}")

            else:
                stack.append(int(t))
        return stack[0]