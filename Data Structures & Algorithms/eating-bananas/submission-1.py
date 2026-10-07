import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = None
        piles.sort()
        l = 1
        r = max(piles)
        while l <= r:
            k = (r - l) //2 + l
            # print(f"t = {t}")
            if self.check(piles, k, h):
                if minK:
                    minK = min(minK, k)
                else:
                    minK = k
                r = k - 1
            else:
                l = k + 1
        return minK


    def check(self, piles, k, h) -> bool:
        hours_taken = 0
        for p in piles:
            # print(f"p/k = {p/k}, math.ceil = {math.ceil(p/k)}")
            hours_taken +=  math.ceil(p / k)
        return hours_taken <= h
