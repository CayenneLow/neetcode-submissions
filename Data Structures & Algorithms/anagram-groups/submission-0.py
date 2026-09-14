class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub = []
        seen_map = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in seen_map:
                sub.append([s])
                seen_map[s_sorted] = len(sub) - 1
            else:
                sub[seen_map[s_sorted]].append(s)
        return sub