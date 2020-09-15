class Employee:
    def __init__(self, name):
        self._name = name

    def toString(self):
        return '{} ({})'.format(self._name, self.typeCode)


class Engineer(Employee):
    @property
    def typeCode(self):
        return 'engineer'


class Manager(Employee):
    @property
    def typeCode(self):
        return 'manager'


class Salesman(Employee):
    @property
    def typeCode(self):
        return 'salesman'


def createEmployee(name, typeCode):
    if typeCode == 'engineer':
        return Engineer(name, typeCode)
    elif typeCode == 'manager':
        return Manager(name, typeCode)
    elif typeCode == 'salesman':
        return Salesman(name, typeCode)
    else:
        raise Exception('Employee cannot be type of {}'.format(typeCode))
