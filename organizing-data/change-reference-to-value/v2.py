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
        self._telephoneNumber = TelephoneNumber(arg, self.officeNumber)

    @property
    def officeNumber(self):
        return self._telephoneNumber.number

    @property.setter
    def officeNumber(self, arg):
        self._telephoneNumber = TelephoneNumber(self.officeAreaCode, arg)

    @property
    def telephoneNumber(self):
        return self._telephoneNumber.toString()


class TelephoneNumber:
    def __init__(self, areaCode, number):
        self._areaCode = areaCode
        self._number = number

    def equals(self, other):
        if not isinstance(other, TelephoneNumber):
            return False

        return self.areaCode == other.areaCode and self.number == other.number

    @property
    def areaCode(self):
        return self._areaCode

    @property
    def number(self):
        return self._number

    @property
    def toString(self):
        return '{}{}'.format(self._areaCode, self._number)
