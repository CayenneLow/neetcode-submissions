class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [None] * (len(nums) + 1)
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        
        for (num, count) in freq_map.items():
            if not buckets[count]:
                buckets[count] = []
            buckets[count].append(num)

        ret = []
        i = len(buckets) - 1
        while i >= 0 and len(ret) < k:
            if buckets[i] is not None:
                for item in buckets[i]:
                    ret.append(item)
            i -= 1
        return ret