class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 0
            hash_table[num] += 1
        l = hash_table.items()
        sorted_l = sorted(l, key=lambda x: x[1], reverse=True)

        ret_list = []
        for i in range(k):
            ret_list.append(sorted_l[i][0])
        return ret_list