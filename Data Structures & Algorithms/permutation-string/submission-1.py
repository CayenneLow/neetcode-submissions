class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = [0] * 26
        for c in s1:
            freq_map[ord(c) - ord('a')] += 1

        freq_map_copy = freq_map.copy()
        l = 0
        r = 0
        while l < len(s2) and r < len(s2):
            index = ord(s2[r]) - ord('a')
            if freq_map_copy[index] > 0:
                freq_map_copy[index] -= 1
                r += 1
            else:
                # Rest the freq_map
                if freq_map_copy == [0] * 26:
                    return True
                freq_map_copy = freq_map.copy()
                l += 1
                r = l
        return freq_map_copy == [0] * 26
        