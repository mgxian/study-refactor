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


def readingOutsideRange(station, min, max):
    return filter(lambda reading: reading["temp"] < min or reading["temp"] > max, station["readings"])


def main():
    operationPlan = {
        "temperatureFloor": 10,
        "temperatureCeiling": 60
    }
    alerts = readingOutsideRange(station,
                                 operationPlan["temperatureFloor"],
                                 operationPlan["temperatureCeiling"])
