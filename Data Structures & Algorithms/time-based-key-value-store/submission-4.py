class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.map.get(key, [])
        arr.append((value, timestamp))
        self.map[key] = arr
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        l = 0
        r = len(self.map[key]) - 1
        # want to find the smallest timestamp >= than requested timestamp
        smallestSoFar = ""
        while l <= r:
            mid = (l + r) // 2
            if self.map[key][mid][1] > timestamp:
                r = mid - 1
            elif self.map[key][mid][1] < timestamp:
                smallestSoFar = self.map[key][mid][0]
                l = mid + 1 
            else:
                smallestSoFar = self.map[key][mid][0]
                break
        return smallestSoFar

