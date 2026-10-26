class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # find pivot
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        # now with pivot, need to check if number is left or right of pivot
        # check if the target is within the bounds on one side, if its not there, then its in the other side
        # with the pivot found, we can assume all numbers on one side is sorted
        l = 0
        r = len(nums) - 1
        # check if target is within the right bound (inclusive)
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
            
        #now we have the sub-array to do BST in
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1

