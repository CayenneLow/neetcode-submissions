class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        a = 0
        while a < len(nums) and nums[a] <= 0:
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue
            l = a + 1
            r = len(nums)-1
            while l < r:
                three_sum = nums[a] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0 :
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            a += 1
        return res
            