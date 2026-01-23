class Solution(object):
    def fib(self, n):
        pn = 0   # previous number F(0)
        cn = 1   # current number F(1)

        # base cases
        if n == 0:
            return pn
        elif n == 1:
            return cn

        # calculate from F(2) to F(n)
        for i in range(2, n + 1):
            nn = pn + cn
            pn = cn
            cn = nn

        return cn


        
        