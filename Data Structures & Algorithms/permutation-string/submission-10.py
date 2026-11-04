class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        freq_s1 = [0] * 26
        for s in s1:
            freq_s1[ord(s) - ord('a')] += 1

        freq_window = [0] * 26
        l = 0
        r = 0
        while r < len(s1):
            freq_window[ord(s2[r]) - ord('a')] += 1
            r += 1

        r = len(s1) - 1
        while r < len(s2):
            print(s2[l:r+1])
            if freq_window == freq_s1:
                return True
            freq_window[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r >= len(s2):
                break
            freq_window[ord(s2[r]) - ord('a')] += 1
        return False
