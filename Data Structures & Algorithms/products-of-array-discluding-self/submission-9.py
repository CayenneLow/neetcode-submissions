class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        after = [1] * len(nums)
        
        sofar = 1
        i = 0
        while i < len(nums):
            before[i] = sofar
            sofar *= nums[i]
            i += 1

        sofar = 1
        i = len(nums) - 1
        while i >= 0:
            after[i] = sofar
            sofar *= nums[i]
            i -= 1

        # print(f"before: {before}")
        # print(f"after: {after}")
        res = [0] * len(nums)
        i = 0
        while i < len(nums):
            res[i] = before[i] * after[i]
            i += 1

        return res
        