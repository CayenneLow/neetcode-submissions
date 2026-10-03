class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        stack = []
        i = 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                floor = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(left, right) - floor
                    w = i - stack[-1] - 1
                    totalArea += h * w
            stack.append(i)
            i += 1
        return totalArea