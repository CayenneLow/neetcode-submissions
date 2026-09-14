class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_map = {}
        for i in s:
            if i not in seen_map:
                seen_map[i] = 1
            else:
                seen_map[i] += 1

        for i in t:
            if i not in seen_map:
                return False
            seen_map[i] -= 1
            if seen_map[i] == 0:
                del seen_map[i]
            
        return len(seen_map) == 0
        