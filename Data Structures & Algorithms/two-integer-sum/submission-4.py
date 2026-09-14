class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        i = 0
        while i < len(nums):
            seen_map[nums[i]] = i
            i += 1
        
        j = 0
        while j < len(nums):
            comp = target - nums[j]
            if comp in seen_map:
                comp_index = seen_map[comp]
                if comp_index == j:
                    j += 1
                    continue
                if comp_index < j:
                    return [comp_index, j]
                else:
                    return [j, comp_index]

            j += 1
