class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        # [1,1,2,8]
        i = 1
        while i < len(nums):
            left[i] = nums[i-1] * left[i-1]
            i += 1

        # [48,24,6,1]
        i = len(nums) - 2
        while i >= 0:
            right[i] = nums[i+1] * right[i+1]
            i -= 1

        res = [0] * len(nums)
        i = 0
        while i < len(nums):
            res[i] = left[i] * right[i]
            i += 1

        return res