class Person:
    def __init__(self, name):
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses

    @property.setter
    def courses(self, aList):
        self._courses = aList


class Course:
    def __init__(self, name, isAdvanced):
        self._name = name
        self._isAdvanced = isAdvanced

    @property
    def name(self):
        return self._name

    @property
    def isAdvanced(self):
        return self._isAdvanced


aPerson = Person("will")
filter(lambda c: c.isAdvanced, aPerson.courses)
aPerson.courses.push(Course("hello", False))
