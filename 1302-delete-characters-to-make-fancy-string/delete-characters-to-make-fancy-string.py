class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) >= 2 and stack[-1] == i and stack[-2] == i:
                continue
            else:
                stack.append(i)

        return "".join(stack)