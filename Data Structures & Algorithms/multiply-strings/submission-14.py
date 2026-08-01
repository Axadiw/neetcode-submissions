class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def num(s):
            return ord(s) - ord('0')

        

        summation_arrays = []
        ret_val = deque()
        max_len = 0
        for i,multiplier in enumerate(num1[::-1]):
            multiplier = num(multiplier)
            acc = 0
            summation_array = deque([0]*i)

            for n in [num(x) for x in num2[::-1]]:
                product = n*multiplier + acc
                acc = product // 10
                summation_array.appendleft((product % 10))
            if acc > 0:
                summation_array.appendleft(acc)

            summation_arrays.append(summation_array)
            max_len = max(max_len,len(summation_array))
        
        print(f"summation_arrays :{summation_arrays} max_len: {max_len}")
        acc = 0
        for i in range(max_len):
            tmp = acc
            for array in summation_arrays:
                if len(array) > 0:
                    tmp += array.pop()
            ret_val.appendleft(str(tmp%10))
            acc = tmp // 10
        if acc > 0:
            ret_val.appendleft(str(acc))

        print(f"ret_val :{ret_val} ret_val len: {len(ret_val)} ret_val)[0]: {ret_val[0]}")    
        while len(ret_val) > 1 and ret_val[0] == '0':
            ret_val.popleft()    
        
        return ''.join(ret_val)
        