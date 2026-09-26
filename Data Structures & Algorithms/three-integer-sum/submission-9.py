class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        a = 0
        while a < len(nums) and nums[a] <= 0:
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue
            l = a + 1
            r = len(nums) - 1
            while l < r:
                tsum = nums[a] + nums[l] + nums[r]
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    # move inwards
                    r -= 1
                    l += 1
                    # to avoid duplicate outcomes, move the left pointer up
                    # no need to move the right pointer up because if left number (and number at 'a' position) is
                    # different, it is impossible to have an answer with the same right pointer
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            a += 1
        return res