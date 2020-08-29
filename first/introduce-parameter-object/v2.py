station = {
    "name": "ZB1",
    "readings": [
        {"temp": 47, "time": "2016-11-10 09:10"},
        {"temp": 53, "time": "2016-11-10 09:20"},
        {"temp": 58, "time": "2016-11-10 09:30"},
        {"temp": 53, "time": "2016-11-10 09:40"},
        {"temp": 51, "time": "2016-11-10 09:50"},
    ]
}


class NumberRange:
    def __init__(self, min, max):
        self.__min = min
        self.__max = max

    def min(self):
        return self.__min

    def max(self):
        return self.__max

    def contains(self, value):
        return self.__min <= value <= self.__max


def readingOutsideRange(station, numberRange):
    return filter(lambda reading: not numberRange.contains(reading["temp"]), station["readings"])


def main():
    operationPlan = {
        "temperatureFloor": 10,
        "temperatureCeiling": 60
    }
    numberRange = NumberRange(
        operationPlan["temperatureFloor"], operationPlan["temperatureCeiling"])
    alerts = readingOutsideRange(station, numberRange)
