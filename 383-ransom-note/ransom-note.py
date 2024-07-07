# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         i = 0
#         j = 0
#         x = sorted(magazine)
#         y = sorted(ransomNote)
#         while i < len(y) and j < len(x):
#             if y[i] == x[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
        
#         return len(y) == i
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False