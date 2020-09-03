import time


class Customer:
    def __init__(self, name, discountRate):
        self._name = name
        self._discountRate = discountRate
        self._contract = CustomerContract(self.dateToday())

    def dateToday(self):
        return time.time()

    @property
    def discountRate(self):
        return self._discountRate

    def becomePreferred(self):
        self._discountRate += 0.03

    def applyDiscount(self, amount):
        return amount.subtract(amount.multiply(self._discountRate))


class CustomerContract:
    def __init__(self, startDate):
        self._startDate = startDate
