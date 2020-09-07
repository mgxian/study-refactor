class Customer:
    @property.setter
    def discountRate(self, arg):
        self.discountRate = arg

    def applyDiscount(self, aNumber):
        if not self.discountRate:
            return aNumber
        else:
            return aNumber-(self.discountRate*aNumber)
