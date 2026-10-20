class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_freq = [0] * 26
        i = 0
        while i < len(s):
            char_freq[ord(s[i]) - ord('a')] += 1
            char_freq[ord(t[i]) - ord('a')] -= 1
            i += 1

        return char_freq == [0] * 26