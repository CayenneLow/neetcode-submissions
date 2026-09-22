class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        char_to_index = {}
        longest = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in char_to_index:
                l = max(char_to_index[s[r]] + 1,l) # without this max, l can go backwards
            char_to_index[s[r]] = r
            longest = max(longest, r-l+1)
            r += 1
        return longest