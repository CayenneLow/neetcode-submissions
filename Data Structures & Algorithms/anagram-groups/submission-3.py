class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_map = {}
        for s in strs:
            tmp_hash = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                tmp_hash[index] += 1
            key = tuple(tmp_hash)
            if key not in seen_map:
                seen_map[key] = []
            seen_map[key].append(s)
        return list(seen_map.values())