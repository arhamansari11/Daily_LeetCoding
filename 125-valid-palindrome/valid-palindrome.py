class Solution:
    def isPalindrome(self, s: str) -> bool:
        def Palindrome(arr , l , r):
            if l >= r:
                return True
            if arr[l] != arr[r]:
                return False
            return Palindrome(arr , l + 1 , r - 1)
        string = ""
        for i in s:
            if i.isalnum():
                string += i.lower()
        l = 0
        r = len(string) - 1
        return Palindrome(string , l , r)