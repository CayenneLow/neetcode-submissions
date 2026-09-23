class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            currMin = self.minstack[-1]
            newMin = min(val, currMin)
            self.minstack.append(newMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minstack[-1]