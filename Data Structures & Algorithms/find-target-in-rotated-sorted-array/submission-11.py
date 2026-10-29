class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1

        pivot = l
        print(nums[pivot])
        l = 0
        r = len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1

