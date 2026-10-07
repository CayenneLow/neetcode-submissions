class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                (popI, popT) = stack.pop()
                res[popI] = i - popI
            t = (i , temperatures[i])
            stack.append(t)
            i += 1
        return res