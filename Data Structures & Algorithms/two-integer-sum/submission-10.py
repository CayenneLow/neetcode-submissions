class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for (i, num) in enumerate(nums):
            t = target - num
            if t in numset:
                return [numset[t], i]
            numset[num] = i
        return []
            