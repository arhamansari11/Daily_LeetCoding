class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                x = ""
                while stack[-1].isalpha() == True:
                    x = stack.pop() + x
                stack.pop()
                n =""
                while stack and stack[-1].isdigit() == True:
                    n = stack.pop() + n
                
                if n == "":
                    n = 1
                else:
                    n = int(n)
                stack.append(x * n)
        
        return "".join(stack)