class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}
        s = s.split()

        # If the lengths don't match, it's impossible to have a bijection
        if len(pattern) != len(s):
            return False

        for char, word in zip(pattern, s):
            # Case 1: character is already mapped
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False  # mismatch in mapping

            # Case 2: word is already mapped to a different character
            elif word in word_to_char:
                if word_to_char[word] != char:
                    return False  # mismatch in reverse mapping

            # Case 3: new mapping — create both mappings
            else:
                char_to_word[char] = word
                word_to_char[word] = char

        return True
