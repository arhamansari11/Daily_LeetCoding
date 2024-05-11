class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        count = 1
        for i in range(len(word)):
            if word[i] == ch:
                count += i
                break
        if count > 1:
            reverse = word[:count][::-1]
            result = reverse + word[count:]
            return result
        
        return word