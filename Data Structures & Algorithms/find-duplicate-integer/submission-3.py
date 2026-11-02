class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while slow < len(nums) and fast < len(nums):
            if slow == fast and (slow and fast):
                break
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow