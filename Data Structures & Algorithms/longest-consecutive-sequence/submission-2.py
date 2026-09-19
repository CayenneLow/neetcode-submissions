class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        already_processed = set()
        highest_length = 0
        for num in nums:
            if num in already_processed:
                continue
            length = 1
            tmp = num + 1
            while tmp in hash_set:
                already_processed.add(tmp)
                length += 1
                tmp += 1
            if length > highest_length:
                highest_length = length
            already_processed.add(num)
        return highest_length