class Person:
    def __init__(self, name, officeAreaCode, officeNumber):
        self._name = name
        self._officeAreaCode = officeAreaCode
        self._officeNumber = officeNumber
        self._telephoneNumber = TelephoneNumber(officeAreaCode, officeNumber)

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, arg):
        self._name = arg

    @property
    def officeAreaCode(self):
        return self._telephoneNumber.areaCode

    @property.setter
    def officeAreaCode(self, arg):
        self._telephoneNumber.areaCode = arg

    @property
    def officeNumber(self):
        return self._telephoneNumber.number

    @property.setter
    def officeNumber(self, arg):
        self._telephoneNumber.number = arg

    @property
    def telephoneNumber(self):
        return self._telephoneNumber.toString()


class TelephoneNumber:
    def __init__(self, areaCode, number):
        self._areaCode = areaCode
        self._number = number

    @property
    def areaCode(self):
        return self._areaCode

    @property.setter
    def areaCode(self, arg):
        self._officeAreaCode = arg

    @property
    def number(self):
        return self._number

    @property.setter
    def number(self, arg):
        self._officeNumber = arg

    @property
    def toString(self):
        return '{}{}'.format(self._areaCode, self._number)
