class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for (i, t) in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][1]:
                (popI, popT) = stack.pop()
                res[popI] = i - popI
            stack.append((i,t))
        return res