class Solution:
    def repeatedCharacter(self, s: str) -> str:
        set_s = set()

        for char in s:
            if char in set_s:
                return char
            set_s.add(char)

