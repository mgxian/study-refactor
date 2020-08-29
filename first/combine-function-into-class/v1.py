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


def client1():
    aReading = acquireReading()
    baseCharge = baseRate(
        aReading["month"], aReading['year'])*aReading['quantity']


def client2():
    aReading = acquireReading()
    base = baseRate(aReading["month"], aReading['year'])*aReading['quantity']
    taxableCharge = max(0, base-taxThreshold(aReading["year"]))


def client3():
    aReading = acquireReading()
    baseChargeAmount = calculateBaseCharge(aReading)


def calculateBaseCharge(aReading):
    return baseRate(aReading["month"], aReading['year'])*aReading['quantity']
