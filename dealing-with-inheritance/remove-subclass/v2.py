class Person:
    def __init__(self, name, genderCode):
        self._name = name
        self._genderCode = genderCode or 'X'

    @property
    def name(self):
        return self._name

    @property
    def genderCode(self):
        return self._genderCode

    @property
    def isMale(self):
        return self.genderCode == 'M'


def createPerson(name, genderCode):
    if genderCode == 'M':
        return Person(name, 'M')
    elif genderCode == 'F':
        return Person(name, 'F')
    else:
        return Person(name, 'X')


def isMale(person):
    return person.isMale


people = []
numberOfMales = len(filter(isMale, people))
