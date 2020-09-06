from functools import reduce


class ProductionPlan:
    @property
    def production(self):
        return reduce(lambda x, y: x + y.amount, self._adjustments, 0)

    def applyAdjustment(self, anAdjustment):
        self._adjustments.push(anAdjustment)
