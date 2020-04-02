class UndergroundSystem:

    def __init__(self):
        self.station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.station:
            self.station[stationName]={id: t}
        elif id not in self.station[stationName]:
            self.station[stationName][id]=t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.station:
            self.station[stationName]={id: t}
        elif id not in self.station[stationName]:
            self.station[stationName][id]=t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        startd = self.station[startStation]
        endd = self.station[endStation]
        sm=c=0
        for k,v in startd.items():
            for k1,v1 in endd.items():
                if k==k1 and v1>v:
                    # print(k, k1, v1,v)
                    sm+=v1-v
                    c+=1
        if c!=0:
            return sm/c
        return 0
