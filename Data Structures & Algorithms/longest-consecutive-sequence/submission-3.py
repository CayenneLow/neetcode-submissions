class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in nums:
            if (num - 1) not in num_set:
                # start of a sequence
                length = 1
                tmp = num + 1
                while tmp in num_set:
                    length += 1
                    tmp += 1
                if length > longest:
                    longest = length
        return longest