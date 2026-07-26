import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                tmp = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp2 - tmp)
            elif t == '*':
                tmp = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp * tmp2)

            elif t == '/':
                tmp = stack.pop()
                tmp2 = stack.pop()
                tmp_res = tmp2 / tmp
                stack.append(math.floor(tmp_res) if tmp_res > 0 else math.ceil(tmp_res))            

            else:
                stack.append(int(t))
        return stack[0]