class Solution:
    def isValid(self, s: str) -> bool:
        brac_dic = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in brac_dic:
                if stack and stack[-1] == brac_dic[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False