class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        
        last_pow = 0
        for i in range(1,n+1):
            
            print(f"pow for {i} is {int(math.pow(2,last_pow))}")
            dp.append(1 + dp[i - int(math.pow(2,last_pow))])
            if i == math.pow(2,last_pow):
                last_pow += 1
            
            
            

        return dp
            
        