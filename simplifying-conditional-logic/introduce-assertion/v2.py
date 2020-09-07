class Customer:
    @property.setter
    def discountRate(self, arg):
        assert arg is None or arg >= 0
        self.discountRate = arg

    def applyDiscount(self, aNumber):
        if not self.discountRate:
            return aNumber
        else:
            assert self.discountRate >= 0
            return aNumber-(self.discountRate*aNumber)
