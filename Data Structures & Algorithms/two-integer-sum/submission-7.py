class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for (i, num) in enumerate(nums):
            if num not in seen_map:
                seen_map[num] = []
            seen_map[num].append(i)

        for (i, num) in enumerate(nums):
            comp = target - num
            if comp in seen_map:
                for n in seen_map[comp]:
                    if n != i:
                        if n < i:
                            return [n ,i]
                        return [i, n]