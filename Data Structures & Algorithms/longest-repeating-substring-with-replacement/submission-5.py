class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        maxLen = 0

        for c in char_set:
            l = 0
            r = 0
            swaps = 0
            while r < len(s):
                if s[r] != c:
                    while swaps == k:
                        if s[l] != c:
                            swaps -= 1
                        l += 1
                    swaps += 1
                maxLen = max(maxLen, r - l + 1)
                r += 1
        return maxLen                 
                    
