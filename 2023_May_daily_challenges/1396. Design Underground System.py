# https://leetcode.com/problems/design-underground-system/

# Time complexity O(1). Space complexity O(n).
class UndergroundSystem:

    def __init__(self):
        self.stations = {}  # (station1, station2): (total_time, count)
        self.check_ins = {} # id: (station1, t1)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station1, t1 = self.check_ins.pop(id)
        key = (station1, stationName)
        if key not in self.stations:
            self.stations[key] = [0, 0]
        self.stations[key][0] += t - t1
        self.stations[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.stations[key][0] / self.stations[key][1]
