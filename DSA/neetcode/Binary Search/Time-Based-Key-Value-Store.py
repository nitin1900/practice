#copy-paste from ai no tried myself...

from collections import defaultdict
class TimeMap:

    def __init__(self):
        # Maps key -> list of [value, timestamp] pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps in set calls are strictly increasing, 
        # appending preserves sorted order.
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # Binary search for the largest timestamp <= the given timestamp
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # valid candidate, try to find a closer (larger) one
                left = mid + 1
            else:
                right = mid - 1
                
        return res