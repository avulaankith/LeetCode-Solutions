class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = n * -1
        if x == 0:
            return 0
        if x == 1:
            return 1
        

        ans = 1.0
        while(n > 0):
            if(n%2 == 1):
                ans = ans * x
            x = x * x
            n = n // 2
        return ans