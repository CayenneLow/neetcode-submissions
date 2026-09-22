class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            freq[i] += 1
        for c in t:
            i = ord(c) - ord('a')
            freq[i] -= 1
        for c in freq:
            if c > 0:
                return False
        return True
            
        