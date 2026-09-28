class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temperature)
        res = [0] * len(temperatures)
        for (i, num) in enumerate(temperatures):
            while len(stack) > 0 and num > stack[-1][1]:
                (popI, popT) = stack.pop()
                res[popI] = i - popI
            stack.append((i, num))
        return res