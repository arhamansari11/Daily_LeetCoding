class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(string):
            stack = []

            for i in string:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            
            return ''.join(stack)

        return remove(s) == remove(t)