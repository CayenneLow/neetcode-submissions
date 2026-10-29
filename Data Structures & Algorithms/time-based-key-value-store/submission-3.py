class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(f"set {key} to {value} at {timestamp}")
        if key not in self.map:
            self.map[key] = []
        if len(self.map[key]) <= timestamp:
            len_to_extend = timestamp - len(self.map[key]) + 1
            self.map[key].extend([""] * len_to_extend)
        self.map[key][timestamp] = value
        # print(self.map[key])

    def get(self, key: str, timestamp: int) -> str:
        # print(f"get {key} at {timestamp}")
        if key not in self.map:
            return ""
        
        i = timestamp
        if timestamp >= len(self.map[key]):
            i = len(self.map[key]) - 1

        while i >= 0 and self.map[key][i] == "":
            # print(i)
            i -= 1

        if i < 0:
            return ""
        return self.map[key][i]
        
