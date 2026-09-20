class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        for c in counts:
            if c > 0:
                return False
        return True