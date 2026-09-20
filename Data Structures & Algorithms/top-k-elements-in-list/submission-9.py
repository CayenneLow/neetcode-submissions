class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for (num, count) in freq.items():
            buckets[count].append(num)

        res = []
        i = len(nums)
        while i >= 0:
            b = buckets[i]
            for num in b:
                if len(res) == k:
                    return res
                res.append(num)
            i -= 1
        return res