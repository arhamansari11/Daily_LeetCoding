class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) >= 2 and i == stack[-1] and i == stack[-2]:
                continue
            else:
                stack.append(i)

        return "".join(stack)