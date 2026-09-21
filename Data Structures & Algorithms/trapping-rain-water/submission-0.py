class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        maxL_so_far = 0
        for (i, num) in enumerate(height):
            maxL[i] = maxL_so_far
            maxL_so_far = max(height[i], maxL_so_far)
        maxR_so_far = 0
        i = len(height) - 1
        while i >= 0:
            maxR[i] = maxR_so_far
            maxR_so_far = max(height[i], maxR_so_far)
            i -= 1

        total = 0
        for (i, num) in enumerate(height):
            boundary = min(maxL[i], maxR[i])
            val = boundary - height[i]
            if val > 0:
                total += val
        return total