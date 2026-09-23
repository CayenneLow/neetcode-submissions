class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for s in tokens:
            if s == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 + num2)
            elif s == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif s == "*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 * num2)
            elif s == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(int(num1 / num2))
            else:
                stack.append(int(s))
        return stack.pop()
                