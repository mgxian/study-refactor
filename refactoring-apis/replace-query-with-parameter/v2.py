thermostat = {}


class HeatingPlan:
    @property
    def targetTemperature(self):
        return self.targetTemperature(thermostat.selectedTemperature)

    def targetTemperature(self, selectedTemperature):
        if selectedTemperature > self._max:
            return self._max
        elif selectedTemperature < self._min:
            return self._min
        else:
            return selectedTemperature


def setToHeat():
    pass


def setToCool():
    pass


def setOff():
    pass


thePlan = HeatingPlan()
if thePlan.targetTemperature(thermostat.selectedTemperature) > thermostat.currentTemperature:
    setToHeat()
elif thePlan.targetTemperature(thermostat.selectedTemperature) < thermostat.currentTemperature:
    setToCool()
else:
    setOff()
