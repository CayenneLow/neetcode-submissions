class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = [0] * 26
        s1_freq = [0] * 26

        l = 0
        r = 0
        while r < len(s1):
            s1_freq[ord(s1[r]) - ord('a')] += 1
            window[ord(s2[r]) - ord('a')] += 1
            r += 1
        
        if window == s1_freq:
            return True
        

        while r < len(s2):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1

            if window == s1_freq:
                return True
        return False

            
        
