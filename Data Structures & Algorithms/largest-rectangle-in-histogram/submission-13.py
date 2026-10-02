class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for (i, h) in enumerate(heights):
            # print(stack)
            start = i 
            while len(stack) > 0 and h < stack[-1][1]:
                # print(stack)
                (popI, popH) = stack.pop()
                start = popI
                area = (i - popI) * popH
                maxArea = max(maxArea, area)
            stack.append((start, h))

        while len(stack) > 0:
            # print(stack)
            (popI, popH) = stack.pop()
            area = (len(heights) - popI) * popH
            maxArea = max(maxArea, area)

        return maxArea