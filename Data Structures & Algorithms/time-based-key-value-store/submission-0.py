class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.ds[key]
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            mid_timestamp = values[mid][1]

            if mid_timestamp == timestamp:
                return values[mid][0]
            elif mid_timestamp < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
