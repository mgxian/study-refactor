class Room:
    pass


class HeatingPlan:
    def withinRange(self, bottom, top):
        return bottom >= self._temperatureRange.low and top <= self._temperatureRange.high


aRoom = Room()
aPlan = HeatingPlan()
alerts = []
low = aRoom.daysTempRange.low
high = aRoom.daysTempRange.high
if not aPlan.withinRange(low, high):
    alerts.push("room temperature went outside range")
