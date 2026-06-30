class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = []
        self.ds[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.ds:
            values = self.ds[key]
        else:
            values = []

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
            

