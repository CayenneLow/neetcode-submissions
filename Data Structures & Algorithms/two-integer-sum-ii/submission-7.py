class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (i, num) in enumerate(numbers):
            index = self.find(numbers, i+1, len(numbers)-1, target-num)
            if index > 0:
                return [i+1, index+1]
            
    
    def find(self, numbers: List[int], start_index: int, end_index: int, target:int) -> int:
        if end_index < start_index:
            return 0
        mid = (end_index - start_index) // 2 + start_index
        if target == numbers[mid]:
            return mid
        elif target > numbers[mid]:
            return self.find(numbers, mid+1, end_index, target)
        else:
            return self.find(numbers, start_index, mid - 1, target)

                