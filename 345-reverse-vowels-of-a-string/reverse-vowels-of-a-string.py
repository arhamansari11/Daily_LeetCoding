class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        vowels = "aeiouAEIOU"
        for i in s:
            if i in vowels:
                arr.append(i)
        arr.reverse()
        result = []
        index = 0
        for i in s:
            if i in vowels:
                result.append(arr[index])
                index += 1
            else:
                result.append(i)
        
        return "".join(result)