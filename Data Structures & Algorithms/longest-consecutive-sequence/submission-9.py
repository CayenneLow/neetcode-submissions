class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hash_map = defaultdict(int)
        for num in nums:
            if hash_map[num]:
                continue
            hash_map[num] = hash_map[num-1] + hash_map[num+1] + 1
            hash_map[num-hash_map[num-1]] = hash_map[num]
            hash_map[num+hash_map[num+1]] = hash_map[num]
            longest = max(longest, hash_map[num])
        return longest