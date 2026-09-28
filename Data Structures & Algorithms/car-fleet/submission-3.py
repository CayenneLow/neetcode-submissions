class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        combined.sort(key = lambda x: x[0], reverse=True)
        # print(combined)

        arrivals = [0.0] * len(combined)
        for i in range(len(combined)):
            arrivals[i] = (target - combined[i][0])/combined[i][1]
        
        stack = []
        for a in arrivals:
            # print(stack)
            if len(stack) == 0 or a > stack[-1]:
                stack.append(a)
        return len(stack)