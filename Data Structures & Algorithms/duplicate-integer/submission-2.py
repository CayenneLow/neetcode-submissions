class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_map = set()
        for num in nums:
            if num in seen_map:
                return True
            seen_map.add(num)
        return False