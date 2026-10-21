class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_map = defaultdict(int)
        for n in nums:
            if not num_map[n]:
                num_map[n] = num_map[n-1] + num_map[n+1] + 1
                num_map[n - num_map[n-1]] = num_map[n]
                num_map[n + num_map[n+1]] = num_map[n]
                res = max(res, num_map[n])
        return res