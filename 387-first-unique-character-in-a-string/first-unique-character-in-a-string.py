class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = Counter(s)
        
        for i, val in enumerate(s):
            if char[val] == 1:
                return i
        return -1



            



            
        