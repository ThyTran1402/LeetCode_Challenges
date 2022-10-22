class UndergroundSystem:

    def __init__(self):
        self.checkIn_hashMap = {}
        self.routeTotalTime = defaultdict(int)
        self.routeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIn_hashMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn_hashMap = self.checkIn_hashMap.pop(id)  #remove the id to avoid making Hashtable big
        routeName = (checkIn_hashMap[0], stationName)
        
        self.routeTotalTime[routeName] += t - checkIn_hashMap[1]
        self.routeCount[routeName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeName = (startStation, endStation)
        return self.routeTotalTime[routeName] / self.routeCount[routeName]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)