class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_set = {}
        for c in t:
            char_set[c] = char_set.get(c, 0) + 1 
        need = len(char_set)
        have = 0

        res = "" 
        l = 0
        r = 0
        curr_freq = {}
        while r < len(s):
            if s[r] in char_set:
                curr_freq[s[r]] = curr_freq.get(s[r], 0) + 1
                if curr_freq[s[r]] == char_set[s[r]]:
                    have += 1
            while have == need:
                if res == "" or ((r-l+1) < len(res)):
                    res = s[l:r+1]
                if s[l] in curr_freq:
                    curr_freq[s[l]] -= 1
                    if curr_freq[s[l]] == (char_set[s[l]] - 1):
                        have -= 1
                l += 1
            r += 1
        return res