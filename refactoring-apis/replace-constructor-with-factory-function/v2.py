class Employee:
    def __init__(self, name, typeCode):
        self._name = name
        self._typeCode = typeCode

    @property
    def name(self):
        return self._name

    @property
    def typeCode(self):
        return self._typeCode

    @staticmethod
    @property
    def legalTypeCode():
        return {
            "E": "Engineer",
            "M": "Manager",
            "S": "Salesman"
        }


def createEmployee(name, typeCode):
    return Employee(name, typeCode)


def createEngineer(name):
    return Employee(name, 'E')


name = 'will'
typeCode = 'E'
candidate = createEmployee(name, typeCode)


leadEngineerName = 'mgxian'
leadEngineer = createEngineer(leadEngineerName)
