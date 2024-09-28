class Solution:
    def fib(self, n: int) -> int:
        def fibonacci(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            ans = fibonacci(n-1) + fibonacci(n-2)
            return ans
            
        return fibonacci(n)