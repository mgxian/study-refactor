class Person:
    def __init__(self, name, officeAreaCode, officeNumber):
        self._name = name
        self._officeAreaCode = officeAreaCode
        self._officeNumber = officeNumber

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, arg):
        self._name = arg

    @property
    def officeAreaCode(self):
        return self._officeAreaCode

    @property.setter
    def officeAreaCode(self, arg):
        self._officeAreaCode = arg

    @property
    def officeNumber(self):
        return self._officeNumber

    @property.setter
    def officeNumber(self, arg):
        self._officeNumber = arg

    @property
    def telephoneNumber(self):
        return '{}{}'.format(self._officeAreaCode, self._officeNumber)
