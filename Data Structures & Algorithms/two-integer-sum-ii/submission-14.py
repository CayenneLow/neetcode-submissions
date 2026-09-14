class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (i, num) in enumerate(numbers):
            t = target - num
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = (r-l) // 2 + l
                if numbers[mid] == t:
                    return [i + 1, mid + 1]
                elif t > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid -1