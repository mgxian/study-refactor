class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    @property.setter
    def department(self, arg):
        self._department = arg


class Department:
    def __init__(self, chargeCode, manager):
        self._chargeCode = chargeCode
        self._manager = manager

    @property
    def chargeCode(self):
        return self._chargeCode

    @property.setter
    def chargeCode(self, arg):
        self._chargeCode = arg

    @property
    def manager(self):
        return self._manager

    @property.setter
    def manager(self, arg):
        self._manager = arg


aPerson = Person()
manager = aPerson.department.manager
