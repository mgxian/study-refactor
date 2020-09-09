class Room:
    pass


class HeatingPlan:
    def withinRange(self, aNumberRange):
        return aNumberRange.low >= self._temperatureRange.low and aNumberRange.high <= self._temperatureRange.high


aRoom = Room()
aPlan = HeatingPlan()
alerts = []
if not aPlan.withinRange(aRoom.daysTempRange):
    alerts.push("room temperature went outside range")
