class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if len(stack) >= 2:
                if i == "+":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op1 + op2)
                    continue
                elif i == "-":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 - op1)
                    continue
                elif i == "*":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 * op1)
                    continue
                elif i == "/":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(int(op2 / op1))
                    continue
                
            stack.append(int(i))

        return stack[0]

                