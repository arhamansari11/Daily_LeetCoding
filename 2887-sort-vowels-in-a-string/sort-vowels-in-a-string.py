class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        arr = []
        for i in s:
            if i in vowels:
                arr.append(i)
        arr.sort()
        result = []
        index = 0
        for i in s:
            if i in vowels:
                result.append(arr[index])
                index += 1
            else:
                result.append(i)
        
        return "".join(result)