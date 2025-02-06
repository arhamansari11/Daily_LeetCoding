class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        characters = list(s)
        left = 0
        right = len(characters) - 1
        while left < right:
            if characters[left] in vowel and characters[right] in vowel:
                characters[left] , characters[right] = characters[right] , characters[left]
                left += 1
                right -= 1
            
            if characters[left] not in vowel:
                left += 1
            
            elif characters[right] not in vowel:
                right -= 1

        return "".join(characters)