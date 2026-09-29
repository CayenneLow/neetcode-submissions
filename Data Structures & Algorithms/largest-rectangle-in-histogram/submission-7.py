class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for (i, h) in enumerate(heights):
            start = i 
            while len(stack) > 0 and h < stack[-1][0]:
                (popH, popI) = stack.pop()
                start = popI
                area = popH * (i - popI)
                maxArea = max(maxArea, area)
            stack.append((h,start))

        for (popH, popI) in stack:
            area = popH * (len(heights) - popI)
            maxArea = max(maxArea, area)
        return maxArea