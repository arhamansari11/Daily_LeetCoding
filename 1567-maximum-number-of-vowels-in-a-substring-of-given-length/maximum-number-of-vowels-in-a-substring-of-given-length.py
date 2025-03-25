class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Step 1: Compute initial vowel count for first k characters
        count = 0  
        for i in range(k):  
            if s[i] in vowels:
                count += 1  

        max_count = count  # Store the max vowel count
        
        # Step 2: Slide the window across the string
        for i in range(k, len(s)):  # Start from index k
            if s[i] in vowels:  
                count += 1  # Add new character's vowel count
            if s[i - k] in vowels:  
                count -= 1  # Remove character that is sliding out
            
            max_count = max(max_count, count)  # Update max vowels seen
        
        return max_count
