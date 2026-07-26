class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pali = {}
        def is_palindrome(s1: str) -> bool:
            if s1 in pali:
                return pali[s1]
                
            if len(s1) == 0:
                return False
            if len(s1) == 1:
                return True

            start = 0
            end = len(s1) - 1

            while start < end:
                if s1[start] != s1[end]:
                    pali[s1] = False
                    return False
                
                start += 1
                end -= 1
            
            pali[s1] = True
            return True
        
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
        seens = set()

        def helper(i):
            if i > len(s):
                return
            
            strings = divide_string(s, curr)
            if len(strings) > 0:
                repro = ','.join(strings)
                if not repro in seens:
                    ret_val.append(strings)
                    seens.add(repro)       
            
            curr.append(i)
            helper(i+1)
            curr.pop()

            helper(i+1)

        helper(0)
        return ret_val