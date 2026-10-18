class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for (i, n) in enumerate(nums):
            hash_set[n] = i

        for (i, n) in enumerate(nums):
            t = target - n
            if t in hash_set and hash_set[t] != i:
                return [i, hash_set[t]]
        return [] 
            