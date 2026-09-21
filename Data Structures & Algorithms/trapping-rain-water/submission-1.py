class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[len(height) - 1]

        total = 0

        l = 0
        r = len(height) - 1
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])


            if height[l] < height[r]:
                l += 1
                val = maxL - height[l]
                if val > 0:
                    total += val
            else:
                r -= 1
                val = maxR - height[r]
                if val > 0:
                    total += val
        return total

            