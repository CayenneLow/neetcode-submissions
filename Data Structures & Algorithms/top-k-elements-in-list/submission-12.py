class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        for r in range(len(nums) + 1):
            buckets.append([] * r)

        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        for (num, freq) in freqs.items():
            buckets[freq].append(num)

        res = []
        i = len(buckets) - 1
        while i >= 0 and len(res) < k:
            j = 0
            bucket = buckets[i]
            while j < len(bucket) and len(res) < k:
                res.append(bucket[j])
                j += 1
            i -= 1
        return res