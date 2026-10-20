class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        l = list(freq.items())
        l.sort(key=lambda x: x[1], reverse=True)
        res = l[:k]
        return [r[0] for r in res]