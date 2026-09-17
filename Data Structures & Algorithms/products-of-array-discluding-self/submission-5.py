class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        i = 1
        while i < len(nums):
            pref[i] = pref[i-1] * nums[i-1]
            i += 1
        i = len(nums) - 2
        while i >= 0:
            suff[i] = suff[i+1] * nums[i+1]
            i -= 1

        res = []
        i = 0
        while i < len(nums):
            res.append(pref[i] * suff[i])
            i += 1
        return res