thermostat = {}


class HeatingPlan:
    @property
    def targetTemperature(self):
        if thermostat.selectedTemperature > self._max:
            return self._max
        elif thermostat.selectedTemperature < self._min:
            return self._min
        else:
            return thermostat.selectedTemperature


def setToHeat():
    pass


def setToCool():
    pass


def setOff():
    pass


thePlan = HeatingPlan()
if thePlan.targetTemperature > thermostat.currentTemperature:
    setToHeat()
elif thePlan.targetTemperature < thermostat.currentTemperature:
    setToCool()
else:
    setOff()
