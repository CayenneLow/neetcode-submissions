class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for (i, num) in enumerate(nums):
            t = target - num
            if t in hash_set:
                return [hash_set[t], i]
            hash_set[num] = i
                        