class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n,a=1,b=2):
            if n==1:
                return a
            return fib(n-1,b,a+b)
        return fib(n)