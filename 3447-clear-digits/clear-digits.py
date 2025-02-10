class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1].isalpha() and i.isdigit():
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)