class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def genderCode(self):
        return 'X'


class Male(Person):
    @property
    def genderCode(self):
        return 'M'


class Female(Person):
    @property
    def genderCode(self):
        return 'F'


people = []
numberOfMales = len(filter(lambda p: isinstance(p, Male), people))
