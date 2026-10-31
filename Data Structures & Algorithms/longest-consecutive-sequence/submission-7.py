class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        freq = {}
        for num in nums:
            if num in freq:
                continue
            left_seq_len = freq.get(num - 1, 0)
            right_seq_len = freq.get(num + 1, 0)
            new_len = left_seq_len + right_seq_len + 1
            freq[num] = new_len
            freq[num - left_seq_len] = new_len
            freq[num + right_seq_len] = new_len
            longest = max(longest, new_len)
        return longest

# [1, 2, 4, 5, 3, 6]

# {
#     1: 1, 5
#     2: 2
#     4: 1
#     5: 2, 5
#     3: 2 + 2 + 1 = 5
# }