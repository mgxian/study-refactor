import copy

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
    rawReading = acquireReading()
    aReading = enrichReading(rawReading)
    baseCharge = aReading['baseCharge']


def client2():
    rawReading = acquireReading()
    aReading = enrichReading(rawReading)
    taxableCharge = aReading['taxableCharge']


def client3():
    rawReading = acquireReading()
    aReading = enrichReading(rawReading)
    baseChargeAmount = aReading["baseCharge"]


def calculateBaseCharge(aReading):
    return baseRate(aReading["month"], aReading['year'])*aReading['quantity']


def enrichReading(original):
    result = copy.deepcopy(original)
    result["baseCharge"] = calculateBaseCharge(result)
    result['taxableCharge'] = max(
        0, result['baseCharge']-taxThreshold(result["year"]))
    return result
