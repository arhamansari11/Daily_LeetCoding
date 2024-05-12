class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        c = 30

        while c >= i:
            ans = pow(4,i)
            if ans == n:
                return True
                break
            i += 1

        return False
    