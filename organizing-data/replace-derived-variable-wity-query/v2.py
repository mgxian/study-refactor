from functools import reduce


class ProductionPlan:
    @property
    def production(self):
        assert self._production == self.calculatedProduction()
        return self._production

    def applyAdjustment(self, anAdjustment):
        self._adjustments.push(anAdjustment)
        self._production += anAdjustment.amount

    def calculatedProduction(self):
        return reduce(lambda x, y: x + y.amount, self._adjustments, 0)
