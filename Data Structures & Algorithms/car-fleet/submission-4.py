class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # O(n)
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        # O(nlogn)
        combined.sort(key = lambda x: x[0], reverse=True)

        # O(n)
        arrivals = [0.0] * len(combined)
        for i in range(len(combined)):
            arrivals[i] = (target - combined[i][0])/combined[i][1]
        
        # O(n)
        stack = []
        for a in arrivals:
            if len(stack) == 0 or a > stack[-1]:
                stack.append(a)

        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        return len(stack)