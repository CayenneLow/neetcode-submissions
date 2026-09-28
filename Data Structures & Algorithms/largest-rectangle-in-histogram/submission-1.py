class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Stores pairs: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop elements that are taller than the current height
            while stack and stack[-1][1] > h:
                popI, popH = stack.pop()
                maxArea = max(maxArea, popH * (i - popI))
                start = popI  # The current height 'h' can extend back to popI
            
            stack.append((start, h))

        # Process any remaining elements in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea