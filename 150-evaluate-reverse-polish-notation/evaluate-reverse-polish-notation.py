class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 + op1)
            elif i == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif i == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 * op1)
            elif i == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 / op1))
            else:
                stack.append(int(i))
            
        return stack[0]