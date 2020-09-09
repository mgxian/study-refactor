def alertForMiscreant(people):
    for p in people:
        if p == "Don":
            setOffAlarms()
            return "Don"

        if p == "John":
            setOffAlarms()
            return "John"
    return ""


def setOffAlarms():
    pass


people = ["Will", "Maria", "John"]
found = alertForMiscreant(people)
