class TimeMap:

    def __init__(self):
        self.tm = {}

    def binary_search(self, array, target):
        left, right = 0, len(array)
        while left < right:
            mid = (right + left) // 2

            if target > array[mid][0]:
                left = mid + 1
            else:
                right = mid
            
        return left
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = [(timestamp, value)]
            
        else:
            ind = self.binary_search(self.tm[key], timestamp)
            if ind < len(self.tm[key]) and self.tm[key][ind][0] == timestamp:
                self.tm[key][ind] = (timestamp, value)
            else:
                self.tm[key].insert(ind, (timestamp, value))
            

    def get(self, key: str, timestamp: int) -> str:
        # print("GET: ", timestamp, key)
        if key in self.tm:
            ind = self.binary_search(self.tm[key], timestamp)
            # print(self.tm[key], ind)
            if ind < len(self.tm[key]) and self.tm[key][ind][0] == timestamp:
                return self.tm[key][ind][1]
            elif ind - 1 >= 0:
                return self.tm[key][ind-1][1]
            else:
                return ""
        return ""
        
