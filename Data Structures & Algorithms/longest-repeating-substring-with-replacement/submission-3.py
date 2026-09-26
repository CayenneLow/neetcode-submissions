class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        maxLen = 0
        
        for c in charSet:
            l = 0
            r = 0
            countOfC = 0
            while r < len(s):
                if s[r] == c:
                    countOfC += 1

                countOfNotC = (r - l + 1) - countOfC
                if countOfNotC > k:
                    if s[l] == c:
                        countOfC -= 1
                    l += 1

                maxLen = max(maxLen, (r - l + 1))
                r += 1
        return maxLen