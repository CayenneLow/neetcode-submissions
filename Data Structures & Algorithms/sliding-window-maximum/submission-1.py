class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def _sift_down(self, i):
        while (2 * i) < len(self.heap):
            largestIndex = i
            if self.heap[largestIndex] < self.heap[2*i]:
                largestIndex = 2 * i
            if (2*i+1) < len(self.heap) and self.heap[largestIndex] < self.heap[2*i+1]:
                largestIndex = 2 * i + 1
            if largestIndex == i:
                break
            self.heap[i], self.heap[largestIndex] = self.heap[largestIndex], self.heap[i]
            i = largestIndex

    def _sift_up(self,i):
        while i > 1 and self.heap[i] > self.heap[i//2]:
            self.heap[i],self.heap[i//2] = self.heap[i//2],self.heap[i]
            i = i // 2
    
    def pop(self):
        self.heap[1], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[1]
        self.heap.pop()
        self._sift_down(1)

    def peek(self):
        return self.heap[1]

    def add(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
        

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max heap Solution with lazy deletion
        res = []
        heap = MaxHeap()
        i = 0
        while i < len(nums):
            heap.add((nums[i],i))
            if i >= k - 1:
                while heap.peek()[1] <= i-k:
                    heap.pop()
                res.append(heap.peek()[0])
            i+=1
        return res
            
            