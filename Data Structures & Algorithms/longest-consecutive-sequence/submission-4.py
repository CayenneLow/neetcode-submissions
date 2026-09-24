class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        res = 0
        for n in nums:
            if n not in  hash_map:
                length_before = hash_map.get(n-1, 0)
                length_after = hash_map.get(n+1,0)
                hash_map[n] = length_before + length_after + 1
                hash_map[n - length_before] = hash_map[n]
                hash_map[n + length_after] = hash_map[n]
                res = max(res, hash_map[n])
        return res
