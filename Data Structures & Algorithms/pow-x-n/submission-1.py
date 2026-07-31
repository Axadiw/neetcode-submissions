class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        x = x if n>0 else 1/x
        acc = x
        n = n if n> 0 else -n
        for _ in range(n-1):
            acc *= x
            print(acc)
        return acc
        