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
                t_sum = nums[a] + nums[l] + nums[r]
                if t_sum > 0:
                    r -= 1
                elif t_sum < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
            a += 1
        return res

# sorted: [-4, -1, -1, 0, 1, 2]