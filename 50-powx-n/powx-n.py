class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power( x , n ):
            if n == 0:
                return 1
            
            return x ** n

        return power( x  , n)