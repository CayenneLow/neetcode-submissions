class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for t in tokens:
            if t == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif t == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif t == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif t == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(t))
        return stack.pop()