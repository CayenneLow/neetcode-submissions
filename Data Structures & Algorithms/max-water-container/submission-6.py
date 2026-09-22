class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        highest = 0
        while l < r:
            height = min(heights[l] , heights[r])
            width = r - l
            volume = width * height
            highest = max(volume, highest)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return highest