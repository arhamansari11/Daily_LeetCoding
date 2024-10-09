class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        result = 0
        for i in s:
            if i == "(":
                balance += 1
            else:
                balance -= 1
             
            if balance == -1:
                result += 1
                balance = 0

        return result + balance
