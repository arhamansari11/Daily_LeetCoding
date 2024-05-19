class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        string =  str(x)

        reverse = string[::-1]

        if str(x) == reverse:
            return True
        
        return False