import time


class Customer:
    def __init__(self, name, discountRate):
        self._name = name
        self._contract = CustomerContract(self.dateToday())
        self._contract._setDiscountRate(discountRate)

    def dateToday(self):
        return time.time()

    @property
    def discountRate(self):
        return self._contract.discountRate

    def _setDiscountRate(self, aNumber):
        self._contract.discountRate = aNumber

    def becomePreferred(self):
        self._contract.discountRate += 0.03

    def applyDiscount(self, amount):
        return amount.subtract(amount.multiply(self.discountRate))


class CustomerContract:
    def __init__(self, startDate, discountRate):
        self._startDate = startDate
        self._discountRate = discountRate

    @property
    def discountRate(self):
        return self._discountRate

    @property.setter
    def discountRate(self, arg):
        self._discountRate = arg
