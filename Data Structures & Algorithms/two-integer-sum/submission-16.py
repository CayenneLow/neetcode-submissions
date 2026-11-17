class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for (i, num) in enumerate(nums):
            t = target - num
            if t in hash_map:
                return [hash_map[t], i]
            hash_map[num] = i
        return []