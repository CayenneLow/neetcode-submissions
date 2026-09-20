class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = {}
        for s in strs:
            char_freq = [0] * 26
            for c in s:
                char_freq[ord(c) - ord('a')] += 1
            tup = tuple(char_freq)
            if tup not in hash_set:
                hash_set[tup] = []
            hash_set[tup].append(s)
        return list(hash_set.values())