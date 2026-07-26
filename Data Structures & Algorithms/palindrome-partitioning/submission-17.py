class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s1: str) -> bool:
            if len(s1) == 0:
                return False
            if len(s1) == 1:
                return True

            start = 0
            end = len(s1) - 1

            while start < end:
                if s1[start] != s1[end]:
                    return False
                
                start += 1
                end -= 1
            
            return True
        
        # def array_containes_palindromes(array):
        #     for item in array:
        #         if not is_palindrome(item):
        #             return False
            
        #     return True
        
        def divide_string(s, divisions):
            ret_val = []

            new_divisions = [0] + divisions + [len(s)]

            for i in range(1, len(new_divisions)):
                new_s = s[new_divisions[i-1]:new_divisions[i]]
                if new_s and is_palindrome(new_s):
                    ret_val.append(new_s)
                else:
                    return []
            return ret_val
        
        ret_val = []
        curr = []

        def helper(i):
            if i > len(s):
                return
            
            strings = divide_string(s, curr)
            # print(f"{curr} -> {strings} len(curr){len(curr)}")
            if len(strings) > 0:
                ret_val.append(strings)
            
            curr.append(i)
            helper(i+1)
            curr.pop()

            helper(i+1)

        helper(0)

        seens = set()
        real_ret_val = []
        for ret in ret_val:
            repro = ','.join(ret)
            if not repro in seens:
                real_ret_val.append(ret)
                seens.add(repro)            
                # print(f"not seen {repro}. adding to the list")
            # else:
                # print(f"{repro} seen")

        return real_ret_val