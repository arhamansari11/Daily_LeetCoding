class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                string += i.lower()

        if string == string[::-1]:
            return True
        else:
            return False