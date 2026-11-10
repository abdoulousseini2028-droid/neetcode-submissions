class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dict:
            self.dict[key] = []
        # dict[key] = [(),(),()]
        self.dict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict.get(key, [])
        if not values:
            return ""
        left, right = 0, len(values)-1
        if not values:
            return ""
        
        while left < right:
            mid = (left + right)//2 +1
            if values[mid][0] > timestamp:
                right = mid -1
            else:
                left = mid
        #in case everything is greater have else statement
        return values[right][1] if values[right][0]<=timestamp else ""
        
