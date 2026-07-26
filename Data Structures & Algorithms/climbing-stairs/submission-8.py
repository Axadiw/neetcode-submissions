# bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [-1] * (n+1)

        steps[0] = 1
        steps[1] = 1

        i = 2
        while i <= n:
            steps[i] = steps[i-1]+steps[i-2]
            i+=1
        return steps[n]