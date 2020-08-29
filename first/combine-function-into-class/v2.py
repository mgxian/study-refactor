reading = {
    "customer": "ivan",
    "quantity": 10,
    "month": 5,
    "year": 2017
}


def acquireReading():
    return reading


def baseRate(month, year):
    return 0.1


def taxThreshold(year):
    return 100


class Reading:
    def __init__(self, data):
        self._customer = data["customer"]
        self._quantity = data["quantity"]
        self._month = data["month"]
        self._year = data["year"]

    @property
    def customer(self):
        return self._customer

    @property
    def quantity(self):
        return self._quantity

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @property
    def baseCharge(self):
        return baseRate(self.month, self.year)*self.quantity

    @property
    def taxableCharge(self):
        return max(0, self.baseCharge - taxThreshold(self.year))


def client1():
    rawReading = acquireReading()
    aReading = Reading(rawReading)
    baseCharge = aReading.baseCharge


def client2():
    rawReading = acquireReading()
    aReading = Reading(rawReading)
    taxableCharge = aReading.taxableCharge


def client3():
    rawReading = acquireReading()
    aReading = Reading(rawReading)
    baseChargeAmount = aReading.baseCharge
