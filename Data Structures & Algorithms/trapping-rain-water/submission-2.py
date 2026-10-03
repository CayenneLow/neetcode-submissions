class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        stack = []
        i = 0
        while i < len(height):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                floor = height[stack.pop()]
                if len(stack) > 0:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - floor
                    w = i - stack[-1] - 1
                    totalArea += h * w
            stack.append(i)
            i += 1
        return totalArea