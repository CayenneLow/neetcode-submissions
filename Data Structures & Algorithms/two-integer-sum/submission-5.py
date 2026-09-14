class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for (i, num) in enumerate(nums):
            t = target - num
            if t in seen_map:
                return [seen_map[t], i]
            seen_map[num] = i            