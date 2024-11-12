class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
                continue
            else:
                stack.append(i)

        return "".join(stack)