class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            char_freq = [0] * 26
            for c in s:
                char_freq[ord(c) - ord('a')] += 1
            key = tuple(char_freq)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())