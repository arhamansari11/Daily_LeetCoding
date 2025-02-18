class Solution:
    def isThree(self, n: int) -> bool:
        i = 1
        count = 0
        while i <= n:
            if n % i == 0:
                count += 1
            i += 1

        if count == 3:
            return True
        else:
            return False
