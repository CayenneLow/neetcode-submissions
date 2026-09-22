class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = set(["(", "{", "["])
        close = set([")", ""])
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            else:
                raise Exception("unknown character")
        return len(stack) == 0