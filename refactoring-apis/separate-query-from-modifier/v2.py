def alertForMiscreant(people):
    if findMiscreant(people) != "":
        setOffAlarms()


def findMiscreant(people):
    for p in people:
        if p == "Don":
            return "Don"

        if p == "John":
            return "John"
    return ""


def setOffAlarms():
    pass


people = ["Will", "Maria", "John"]
found = findMiscreant(people)
alertForMiscreant(people)
