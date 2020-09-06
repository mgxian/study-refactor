class ProductionPlan:
    @property
    def production(self): return self._production

    def applyAdjustment(self, anAdjustment):
        self._adjustments.push(anAdjustment)
        self._production += anAdjustment.amount
