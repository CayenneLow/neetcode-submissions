class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            timeToReach = (target - p) / s
            if len(stack) == 0 or timeToReach > stack[-1]:
                stack.append(timeToReach)
        return len(stack)