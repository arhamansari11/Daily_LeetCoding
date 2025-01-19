class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        length = len(arr)
        last = len(arr[length-1])
        return last