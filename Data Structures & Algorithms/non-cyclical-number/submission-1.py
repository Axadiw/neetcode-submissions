class Solution:
    def isHappy(self, n: int) -> bool:
        def gimme_digits(n):
            ret_val = []

            while n != 0:
                ret_val.append(n%10)
                n = n//10
            ret_val.reverse()
            return ret_val
        
        seen = set()

        while not n in seen and n != 1:
            seen.add(n)
            n = sum([x*x for x in gimme_digits(n)])            

        return n == 1
        