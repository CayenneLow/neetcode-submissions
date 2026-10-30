class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        final_arr = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                final_arr.append(nums1[i])
                i += 1
            else:
                final_arr.append(nums2[j])
                j += 1
        if i < len(nums1):
            final_arr.extend(nums1[i:]) 
        if j < len(nums2):
            final_arr.extend(nums2[j:]) 
        print(final_arr)

        mid = len(final_arr) // 2
        if len(final_arr) % 2 == 0:
            # even means need to divide two numbers
            return (final_arr[mid] + final_arr[(mid - 1)]) / 2
        return final_arr[mid]