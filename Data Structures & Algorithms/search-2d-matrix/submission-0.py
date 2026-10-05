class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if target >= matrix[mid][0]:
                if self.search(matrix[mid], target):
                    return True
                else:
                    l = mid + 1
            else:
                r = mid - 1
        return False

    def search(self, arr: List[int], target:int) -> bool:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if target == arr[mid]:
                return True
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False