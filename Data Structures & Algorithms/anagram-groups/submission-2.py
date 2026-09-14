class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_map = {}
        for s in strs:
            tmp_hash = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                tmp_hash[i] += 1
            tup = tuple(tmp_hash)
            if tup not in seen_map:
                seen_map[tup] = []
            seen_map[tup].append(s)
        return list(seen_map.values())